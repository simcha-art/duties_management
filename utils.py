# ============================================================================
# utils.py
# אחריות: פונקציות עזר שחוזרות על עצמן
# ============================================================================

import data


def find_soldier_by_id(soldier_id: str) -> dict | None:
    """
    מחפשת חייל לפי id ומחזירה אותו.
    
    סוג: פונקציית עזר (Helper Function)
    
    מקבלת:
        soldier_id (str): מספר אישי של החייל
    
    מחזירה:
        dict | None: מילון של החייל אם נמצא, None אם לא נמצא
    
    זורקת: כלום - מחזירה None במקרה שלא נמצא
    
    """
    is_find = False
    for sold in data.soldiers:
        if sold["id"] == soldier_id:
            is_find = True
    return is_find


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """
    מחפשת תורנות לפי שם ברשימת תורנויות.
    
    סוג: פונקציית עזר (Helper Function)
    
    מקבלת:
        duties (list): רשימת תורנויות
        duty_name (str): שם התורנות לחיפוש
    
    מחזירה:
        dict | None: מילון של התורנות אם נמצאה, None אם לא נמצאה
    
    זורקת: כלום - מחזירה None במקרה שלא נמצא
    
    """
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return

def is_valid_status(status: str) -> bool:
    """
    בודקת אם סטטוס הוא חוקי
    
    סוג: פונקציית validation (בדיקת תקינות)
    
    מקבלת:
        status (str): הסטטוס לבדיקה
    
    מחזירה:
        bool: True אם הסטטוס חוקי (pending/completed/missed)
              False אם לא חוקי
    
    זורקת: כלום - תמיד מחזירה bool
    
    """

    VALID_STATUS = ("pending","completed","missed")
    return status in VALID_STATUS

def is_valid_name(name: str) -> bool:
    """
    בודקת אם שם הוא תקין (לא ריק).
    
    סוג: פונקציית validation (בדיקת תקינות)
    
    מקבלת:
        name (str): השם לבדיקה
    
    מחזירה:
        bool: True אם השם תקין (לא ריק)
              False אם ריק
    
    זורקת: כלום - תמיד מחזירה bool
    
    """
    name = name.strip()
    return bool(name)

def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """
    בודקת אם לחייל יש תורנות עם שם מסוים.
    
    סוג: פונקציית validation (בדיקת תקינות)
    
    מקבלת:
        soldier (dict): מילון של חייל
        duty_name (str): שם התורנות לבדיקה
    
    מחזירה:
        bool: True אם התורנות קיימת לחייל
              False אם לא קיימת
    
    זורקת: כלום - תמיד מחזירה bool
    
    למה הפונקציה קיימת:
    בדיקה זו משמשת בהוספת תורנות (למנוע כפילויות).
    הפרדה של הלוגיקה למקום אחד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    pass


def is_valid_day(day: str) -> bool:
    """
    בודקת אם יום הוא חוקי (לא שישי או שבת).
    
    סוג: פונקציית validation (בדיקת תקינות)
    
    מקבלת:
        day (str): היום לבדיקה
    
    מחזירה:
        bool: True אם היום חוקי (sunday-thursday)
              False אם לא חוקי או אסור (friday/saturday או ערך לא תקין)
    
    זורקת: כלום - תמיד מחזירה bool
    """

    VALID_DAYS = ("sunday", "monday", "tuesday", "wednesday", "thursday")
    return day.lower() in VALID_DAYS

