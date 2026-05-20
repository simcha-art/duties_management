"""
מערכת ניהול תורנויות חיילים
"""

# ============================================================================
# main.py
# אחריות: תפריט ראשי, קלט מהמשתמש, ניתוב לפונקציות
# ============================================================================
import soldiers_management
import duty_management




def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.
    
    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)
    
    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    message = """
=======================
Options:
1. add soldier
2. remove soldier
3. view soldiers
4. add duty
5. update duty status
6. view_soldier_duties
7.exit
"""
    print(message)


def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.
    
    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    
    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    choice = input("Enter your choice (1-7): ")
    return choice

# show_menu()
# print(get_user_choice())


def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    name = input("Enter soldier's name: ")
    id = input("Enter soldier's ID: ")

    soldiers_management.add_soldier(id, name)


def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    id = input("Enter soldier's ID: ")
    soldiers_management.remove_soldier(id)




def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    print(soldiers_management.get_all_soldiers())


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    id_soldier = input("Enter soldier's ID: ")
    duty_name = input("Enter duty name: ")
    day = input("Enter the day of the duty: ")
    
    duty_management.add_duty_to_soldier(id_soldier, duty_name, day)





def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = input("Enter soldier's ID: ")
    duty_name = input("Enter duty's name: ")
    new_status = input("Enter the new status: ")

    duty_management.update_duty_status(soldier_id, duty_name, new_status)



def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = input("Enter soldeir's ID: ")
    print(duty_management.get_soldier_duties(soldier_id))


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    while True:
        try:
            show_menu()
            choice = get_user_choice()
            if choice == "1":
                handle_add_soldier()
                print("operation_completed_successfully")
            
            elif choice == "2":
                handle_remove_soldier()
                print("operation_completed_successfully")


            elif choice == "3":
                handle_view_soldiers()

            elif choice == "4":
                handle_add_duty()
                print("operation_completed_successfully")


            elif choice == "5":
                handle_update_duty_status()
                print("operation_completed_successfully")

            elif choice == "6":
                handle_view_soldier_duties()

            elif choice == "7":
                break
        except (KeyError, ValueError) as e:
            print(e)

if __name__ == "__main__":
    main()



