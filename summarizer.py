# שימו לב לאחר שהגדרתם את נתיב התיקייה להריץ ע"י python summarizer.py בטרמינל

import os

# מגדירים את נתיב התיקייה שמכילה את הקבצים
dir_path = r'C:\your file path'

# משיגים את שם התיקייה מתוך הנתיב
dir_name = os.path.basename(dir_path)

# מגדירים את שם הקובץ התוצר, בשילוב של שם התיקייה
output_file = f'{dir_name}.txt'

# מגדירים את הנתיב המלא של הקובץ התוצר, בתוך אותה התיקייה המקורית
output_file_path = os.path.join(dir_path, output_file)

# פותחים את הקובץ התוצר לכתיבה
with open(output_file_path, 'w', encoding='utf-8') as f:
    # עוברים על כל הקבצים בתיקייה
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        
        # מוודאים שזה קובץ רגיל (ולא תיקייה)
        if os.path.isfile(file_path):
            # מדפיסים שורות של כוכביות כפרדה ויזואלית
            f.write('*' * 80 + '\n')
            
            # מדפיסים כותרת מודגשת לקובץ
            f.write(f'** {filename} **\n\n')
            
            # מדפיסים הערה מסבירה לפני התוכן של הקובץ
            f.write('# הקוד הבא מתוך הקובץ:\n\n')
            
            # קוראים את תוכן הקובץ ומדפיסים אותו לקובץ התוצר
            with open(file_path, 'r', encoding='utf-8') as content_file:
                f.write(content_file.read() + '\n\n')