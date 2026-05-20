# ============================================================================
# soldier_manager.py
# אחריות: לוגיקה עסקית של ניהול חיילים
# ============================================================================
import utils
import data

def add_soldier(soldier_id: str, name: str) -> None:
    """
    מוסיפה חייל חדש למערכת.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (str): מספר אישי של החייל
        name (str): שם החייל
    
    מחזירה:
        None - הפונקציה מוסיפה את החייל או זורקת exception
    
    זורקת:
        ValueError: אם id כבר קיים במערכת
        ValueError: אם name ריק או לא תקין
    
    למה הפונקציה קיימת:
    לוגיקה עסקית טהורה של הוספת חייל.
    מבצעת בדיקות תקינות ומוסיפה את החייל לנתונים.
    לא מטפלת בקלט/פלט - רק בלוגיקה.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    if not utils.is_valid_name(name):
        raise ValueError ("Invalid name")
    if utils.find_soldier_by_id(soldier_id):
        raise ValueError ("soldier id is already exist")
    
    data.soldiers.append({"name": name, "id": soldier_id, "duties": []})



def remove_soldier(soldier_id: str) -> None:
    """
    מסירה חייל מהמערכת לפי id.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (str): מספר אישי של החייל
    
    מחזירה:
        None - הפונקציה מסירה את החייל או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הסרת חייל.
    מבצעת בדיקת קיום ומסירה מהנתונים.
    זורקת exception במקרה שהחייל לא קיים.
    """
    soldier = utils.find_soldier_by_id(soldier_id)
    if not soldier :
        raise KeyError ("Soldier with this id does not exist")
    data.soldiers.remove(soldier)




def get_all_soldiers() -> list:
    """
    מחזירה את רשימת כל החיילים במערכת.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת: כלום
    
    מחזירה:
        list: רשימה של מילונים, כל מילון מייצג חייל
              רשימה ריקה אם אין חיילים
    
    זורקת: כלום - תמיד מחזירה רשימה (ריקה או מלאה)
    
    למה הפונקציה קיימת:
    גישה לנתונים בצורה מבוקרת.
    מאפשר לקבל את הנתונים מבלי לגשת ישירות למשתנה הגלובלי.
    """
    return data.soldiers.copy()


