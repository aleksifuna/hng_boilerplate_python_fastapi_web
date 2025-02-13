from pydantic import BaseModel, EmailStr
from datetime import datetime


class EmailSchema(BaseModel):
    """
    pydantic model for data validation and serialization
    """

    email: EmailStr
    

class EmailRetrieveSchema(EmailSchema):

    class Config:
        from_attributes = True

class NewsletterBase(BaseModel):
    title: str
    description: str
    content: str 
    created_at: datetime
    updated_at: datetime

class SingleNewsletterResponse(BaseModel):
    """Schema for single newsletter
    """
    status_code: int = 200
    message: str
    success: bool = True
    data: NewsletterBase

