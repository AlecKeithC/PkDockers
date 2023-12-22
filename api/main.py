from pydantic import BaseModel
from pydantic_settings import BaseSettings
from fastapi import FastAPI, Depends, HTTPException
import psycopg2
from typing import List
from datetime import datetime
import threading
import time
class Settings(BaseSettings):
    DATABASE_URL: str = "postgres://admin:detectaudec@192.168.1.81:32783/parkingdb"

settings = Settings()

class Parking(BaseModel):
    id: int
    free_spaces: int
    total_spaces: int
    pk_name: str
    latitude: float
    longitude: float
    reduced_capacity: bool
    academico: bool
    estudiante: bool
    administrativo: bool
    otro: bool
    active: bool
    last_update: datetime
    estatica:bool
    out_of_range:bool

class ParkingResponse(Parking):
    class Config:
        from_attributes = True
        
app = FastAPI(title="EstacionaUdec API", description="API para el monitoreo de espacios de estacionamiento en el campus universitario", version="1.0")

# Definimos un diccionario que almacena la última actualización y los espacios libres
last_updates = {}

def get_db():
    try:
        conn = psycopg2.connect(settings.DATABASE_URL)
        yield conn
    finally:
        conn.close()

def update_last_updates():
    while True:
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("UPDATE parking SET last_update = %s WHERE estatica = False", (datetime.now(),))
            conn.commit()
        time.sleep(5)

# Iniciar el hilo para actualizar last_update
threading.Thread(target=update_last_updates, daemon=True).start()

@app.get("/parkings/", response_model=List[ParkingResponse])
def read_parkings(conn: psycopg2.extensions.connection = Depends(get_db)):
    global last_updates
    cur = conn.cursor()
    cur.execute("SELECT * FROM parking")
    rows = cur.fetchall()
    parkings = []
    for row in rows:
        parking_id = row[0]
        estatica = row[13]
        last_update = row[12]
        free_spaces = row[1]

        # Si es estática, revisamos si se ha actualizado last_update
        if estatica:
            if parking_id in last_updates:
                last_known_update, last_known_free_spaces = last_updates[parking_id]
                if last_update == last_known_update:
                   free_spaces = last_known_free_spaces

        # Actualizamos el diccionario con los nuevos valores
        last_updates[parking_id] = (last_update, free_spaces)

        parking = ParkingResponse(
            id=row[0], free_spaces=free_spaces, total_spaces=row[2], pk_name=row[3],
            latitude=row[4], longitude=row[5], reduced_capacity=row[6], academico=row[7],
            estudiante=row[8], administrativo=row[9], otro=row[10], active=row[11],
            last_update=last_update, estatica=estatica, out_of_range=row[14]
        )
        parkings.append(parking)

    return parkings
@app.get("/parkings/{parking_id}", response_model=ParkingResponse)
def read_parking(parking_id: int, conn: psycopg2.extensions.connection = Depends(get_db)):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM parking WHERE id = {parking_id}")
    row = cur.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Parking not found")
    parking = ParkingResponse(
        id=row[0], free_spaces=row[1], total_spaces=row[2], pk_name=row[3],
        latitude=row[4], longitude=row[5], reduced_capacity=row[6], academico=row[7],
        estudiante=row[8], administrativo=row[9], otro=row[10], active=row[11], last_update= row[12], estatica = row[13], 
        out_of_range=row[14]
    )
    return parking