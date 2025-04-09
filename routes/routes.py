from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.event import Event, EventCreate, EventResponse, EventUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/events/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.get("/events/", response_model=list[EventResponse])
def read_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

@router.get("/events/{id}", response_model=EventResponse)
def read_event(id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/events/{id}", response_model=EventResponse)
def update_event(id: int, event_data: EventUpdate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    # Verificar si hay atributos faltantes
    data_dict = event_data.model_dump(exclude_unset=True)
    if not data_dict:
        raise HTTPException(status_code=400, detail="No update data provided")
    
    # Identificar qué atributos faltan
    missing_fields = []
    for field in EventUpdate.model_fields.keys():
        if field not in data_dict or data_dict[field] is None:
            missing_fields.append(field)
    
    if missing_fields:
        raise HTTPException(
            status_code=400, 
            detail=f"Missing attributes: {', '.join(missing_fields)}"
        )
    
    # Actualizar el evento si todos los atributos están presentes
    for key, value in data_dict.items():
        setattr(event, key, value)
    
    db.commit()
    return event

@router.delete("/events/{id}")
def delete_event(id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"message": "Event deleted"}
