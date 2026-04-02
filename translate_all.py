#!/usr/bin/env python3
"""Translate all Hebrew text to English in the kids-lots-of-triangles-en project."""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

def read_file(name):
    with open(os.path.join(BASE, name), 'r', encoding='utf-8') as f:
        return f.read()

def write_file(name, content):
    with open(os.path.join(BASE, name), 'w', encoding='utf-8') as f:
        f.write(content)

def r(content, old, new):
    """Replace all occurrences."""
    return content.replace(old, new)

# ============================================================
# index.html
# ============================================================
def translate_index():
    c = read_file('index.html')

    # lang/dir
    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')

    # title
    c = r(c, 'מרובעים עם אלכסונים - הרבה משולשים - ', 'Quadrilaterals with Diagonals - Lots of Triangles')

    # CSS comments
    c = r(c, '/* Animated highlight - איטי ונעים */', '/* Animated highlight - slow and smooth */')
    c = r(c, '/* קשתות זווית */', '/* Angle arcs */')

    # RTL layout fixes
    c = r(c, 'text-align: right;', 'text-align: left;')
    c = r(c, 'margin-left: 12px;', 'margin-right: 12px;')

    # Greeting
    c = r(c, 'שלום !', 'Hello!')

    # HTML comments
    c = r(c, '<!-- עמוד 1: שאלה סעיף א -->', '<!-- Page 1: Question Part A -->')
    c = r(c, '<!-- עמוד 2: הסבר סעיף א -->', '<!-- Page 2: Explanation Part A -->')
    c = r(c, '<!-- עמוד 3: שאלה סעיף ב -->', '<!-- Page 3: Question Part B -->')
    c = r(c, '<!-- עמוד 4: הסבר סעיף ב -->', '<!-- Page 4: Explanation Part B -->')
    c = r(c, '<!-- עמוד 5: שאלה סעיף ג - עוברים למרובע השני -->', '<!-- Page 5: Question Part C - moving to second quadrilateral -->')
    c = r(c, '<!-- עמוד 6: הסבר סעיף ג -->', '<!-- Page 6: Explanation Part C -->')
    c = r(c, '<!-- עמוד 7: שאלה סעיף ד -->', '<!-- Page 7: Question Part D -->')
    c = r(c, '<!-- עמוד 8: הסבר סעיף ד -->', '<!-- Page 8: Explanation Part D -->')
    c = r(c, '<!-- עמוד סיום -->', '<!-- Final page -->')
    c = r(c, '<!-- מרובע ABCD -->', '<!-- Quadrilateral ABCD -->')
    c = r(c, '<!-- מרובע EFGH -->', '<!-- Quadrilateral EFGH -->')
    c = r(c, '<!-- אלכסונים ABCD -->', '<!-- Diagonals ABCD -->')
    c = r(c, '<!-- אלכסונים EFGH -->', '<!-- Diagonals EFGH -->')
    c = r(c, '<!-- תוויות -->', '<!-- Labels -->')
    c = r(c, '<!-- נקודות חיתוך -->', '<!-- Intersection points -->')
    c = r(c, '<!-- אלכסונים -->', '<!-- Diagonals -->')
    c = r(c, '<!-- קשת זווית קודקודית -->', '<!-- Vertical angle arc -->')

    # Multi-line SVG comment
    c = r(c, 'הציור: שני מרובעים חופפים', 'Drawing: two overlapping quadrilaterals')
    c = r(c, 'מרובע ABCD:', 'Quadrilateral ABCD:')
    c = r(c, 'מרובע EFGH:', 'Quadrilateral EFGH:')
    c = r(c, 'נקודת חיתוך: O(275,200) - מרכז', 'Intersection point: O(275,200) - center')
    c = r(c, 'אלכסונים של ABCD: AC ו-BD נחתכים ב-O', 'Diagonals of ABCD: AC and BD intersect at O')
    c = r(c, 'אלכסונים של EFGH: EG ו-FH נחתכים ב-O', 'Diagonals of EFGH: EG and FH intersect at P')

    # Section headers
    c = r(c, 'תרגיל: שני מרובעים עם אלכסונים', 'Exercise: Two Quadrilaterals with Diagonals')

    # Given box
    c = r(c, '<div><strong>נתון:</strong></div>', '<div><strong>Given:</strong></div>')
    c = r(c, 'ABCD מרובע, האלכסונים AC ו-BD נחתכים ב-O', 'ABCD is a quadrilateral, diagonals AC and BD intersect at O')
    c = r(c, 'EFGH מרובע, האלכסונים EG ו-FH נחתכים ב-P', 'EFGH is a quadrilateral, diagonals EG and FH intersect at P')
    c = r(c, '(O חוצה את AC)', '(O bisects AC)')
    c = r(c, '(O חוצה את BD)', '(O bisects BD)')
    c = r(c, '(P חוצה את EG)', '(P bisects EG)')
    c = r(c, '(P חוצה את FH)', '(P bisects FH)')

    # Instruction
    c = r(c, 'בכל מרובע יש 4 משולשים שנוצרים מהאלכסונים. בואי נמצא משולשים חופפים!',
          "Each quadrilateral has 4 triangles formed by the diagonals. Let's find congruent triangles!")

    # Part headers
    c = r(c, ">סעיף א'<", ">Part A<")
    c = r(c, "סעיף ב' - זוג משולשים נוסף במרובע ABCD", "Part B - Another Pair of Triangles in Quadrilateral ABCD")
    c = r(c, "סעיף ג' - עכשיו במרובע EFGH", "Part C - Now in Quadrilateral EFGH")
    c = r(c, "סעיף ד' - הזוג הרביעי במרובע EFGH", "Part D - The Fourth Pair in Quadrilateral EFGH")

    # Question boxes
    c = r(c, 'הוכיחי ש:', 'Prove that:')
    c = r(c, 'לפי איזה משפט חפיפה?', 'By which congruence theorem?')

    # Answer buttons
    c = r(c, 'צ.צ.צ<br>(צלע-צלע-צלע)', 'SSS<br>(Side-Side-Side)')
    c = r(c, 'צ.ז.צ<br>(צלע-זווית-צלע)', 'SAS<br>(Side-Angle-Side)')
    c = r(c, 'ז.צ.ז<br>(זווית-צלע-זווית)', 'ASA<br>(Angle-Side-Angle)')
    c = r(c, 'צ.צ.ז<br>(צלע-צלע-זווית)', 'SSA<br>(Side-Side-Angle)')

    # Feedback
    c = r(c, 'חשבי: AO=CO (נתון), BO=DO (נתון), והזווית ביניהן ∠AOB=∠COD (זוויות קודקודיות)',
          'Think: AO=CO (given), BO=DO (given), and the angle between them ∠AOB=∠COD (vertical angles)')
    c = r(c, 'שוב יש לנו צלע-זווית-צלע! BO=DO, הזוויות ∠BOC=∠DOA קודקודיות, ו-CO=AO.',
          'Again we have Side-Angle-Side! BO=DO, angles ∠BOC=∠DOA are vertical, and CO=AO.')
    c = r(c, 'אותו עיקרון! EP=GP, הזוויות ∠EPF=∠GPH קודקודיות, ו-FP=HP.',
          'Same principle! EP=GP, angles ∠EPF=∠GPH are vertical, and FP=HP.')
    c = r(c, 'ושוב! FP=HP, הזוויות ∠FPG=∠HPE קודקודיות, ו-GP=EP.',
          'And again! FP=HP, angles ∠FPG=∠HPE are vertical, and GP=EP.')

    # Success messages
    c = r(c, 'נכון מאוד!', 'Exactly right!')
    c = r(c, '>מצוין!<', '>Excellent!<')
    c = r(c, '>מעולה!<', '>Outstanding!<')
    c = r(c, '>יופי!<', '>Great!<')

    # Continue/Next
    c = r(c, 'להמשיך להסבר', 'Continue to Explanation')
    c = r(c, "המשך לסעיף ב'", 'Continue to Part B')
    c = r(c, "המשך לסעיף ג'", 'Continue to Part C')
    c = r(c, "המשך לסעיף ד'", 'Continue to Part D')
    c = r(c, '>סיום<', '>Finish<')

    # Explanation titles
    c = r(c, "הוכחת סעיף א'", 'Proof of Part A')
    c = r(c, "הוכחת סעיף ב'", 'Proof of Part B')
    c = r(c, "הוכחת סעיף ג'", 'Proof of Part C')
    c = r(c, "הוכחת סעיף ד'", 'Proof of Part D')

    # Subtitle with SAS
    c = r(c, 'לפי צ.ז.צ', 'by SAS')

    # Reason cards
    c = r(c, '>צ<', '>S<')
    c = r(c, '>ז<', '>A<')
    c = r(c, '(נתון - O חוצה את AC)', '(Given - O bisects AC)')
    c = r(c, '(זוויות קודקודיות)', '(Vertical angles)')
    c = r(c, '(נתון - O חוצה את BD)', '(Given - O bisects BD)')
    c = r(c, '(נתון - P חוצה את EG)', '(Given - P bisects EG)')
    c = r(c, '(נתון - P חוצה את FH)', '(Given - P bisects FH)')

    # Conclusion cards
    c = r(c, 'לכן:', 'Therefore:')
    c = r(c, '(לפי משפט צ.ז.צ)', '(By SAS congruence theorem)')
    c = r(c, 'מה ניתן להסיק?', 'What can we conclude?')
    c = r(c, '(צלעות מתאימות במשולשים חופפים)', '(Corresponding sides of congruent triangles)')

    # Already proven
    c = r(c, '<div><strong>כבר הוכחנו:</strong></div>', '<div><strong>Already proven:</strong></div>')
    c = r(c, '<div><strong>כבר הוכחנו במרובע ABCD:</strong></div>', '<div><strong>Already proven in quadrilateral ABCD:</strong></div>')

    # Final page
    c = r(c, 'כל הכבוד !', 'Well Done!')
    c = r(c, 'סיימת את כל התרגיל בהצלחה!', 'You completed the entire exercise successfully!')
    c = r(c, 'מצאת את כל המשולשים החופפים:', 'You found all the congruent triangles:')
    c = r(c, 'במרובע ABCD:', 'In quadrilateral ABCD:')
    c = r(c, 'במרובע EFGH:', 'In quadrilateral EFGH:')
    c = r(c, 'סה"כ: ', 'Total: ')
    c = r(c, '8 משולשים', '8 triangles')
    c = r(c, ' ב-4 זוגות חופפים!', ' in 4 congruent pairs!')
    c = r(c, 'כל החפיפות היו לפי צ.ז.צ - בזכות הזוויות הקודקודיות!', 'All congruences were by SAS - thanks to vertical angles!')
    c = r(c, 'להתחיל מחדש', 'Start Over')

    # JS strings
    c = r(c, "'נכון! '", "'Correct! '")
    c = r(c, "'לא נכון. נסי שוב!'", "'Incorrect. Try again!'")

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('index.html', c)
    print('index.html translated')

# ============================================================
# page2.html - Angle calculations
# ============================================================
def translate_page2():
    c = read_file('page2.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')
    c = r(c, 'עבודה לחופשת חנוכה - עמוד 2: חישוב זוויות', 'Hanukkah Break Assignment - Page 2: Angle Calculations')

    # RTL layout fixes
    c = r(c, 'text-align: right;', 'text-align: left;')

    # Greeting
    c = r(c, 'חישוב זוויות - עמוד 2', 'Angle Calculations - Page 2')

    # HTML comments
    c = r(c, '<!-- ==================== תרגיל 1 סעיף א ====================', '<!-- ==================== Exercise 1 Part A ====================')
    c = r(c, '<!-- ==================== תרגיל 1 סעיף ב ====================', '<!-- ==================== Exercise 1 Part B ====================')
    c = r(c, '<!-- ==================== תרגיל 1 סעיף ג ====================', '<!-- ==================== Exercise 1 Part C ====================')
    c = r(c, '<!-- ==================== תרגיל 2 סעיף א ====================', '<!-- ==================== Exercise 2 Part A ====================')
    c = r(c, '<!-- ==================== תרגיל 2 סעיף ב ====================', '<!-- ==================== Exercise 2 Part B ====================')
    c = r(c, '<!-- ==================== תרגיל 2 סעיף ג ====================', '<!-- ==================== Exercise 2 Part C ====================')
    c = r(c, '<!-- ==================== תרגיל 2 סעיף ד ====================', '<!-- ==================== Exercise 2 Part D ====================')
    c = r(c, '<!-- ==================== עמוד סיכום ====================', '<!-- ==================== Summary Page ====================')

    # SVG comments
    c = r(c, '<!-- הבסיס -->', '<!-- Base -->')
    c = r(c, '<!-- צלעות המשולש: A-B שמאל, A-קודקוד ימני (בין C ל-D) -->', '<!-- Triangle sides: A-B left, A-right vertex (between C and D) -->')
    c = r(c, '<!-- קרניים מחלקות מ-A ל-C -->', '<!-- Rays from A to C -->')
    c = r(c, '<!-- קו AD מקווקו - הקו שיוצר זווית 75° עם DE -->', '<!-- Line AD dashed - the line forming 75 angle with DE -->')
    c = r(c, '<!-- קשתות זוויות ב-A -->', '<!-- Angle arcs at A -->')
    c = r(c, '<!-- זווית 3 (סגול) - בין AB לקרן 1 -->', '<!-- Angle 3 (purple) - between AB and ray 1 -->')
    c = r(c, '<!-- זווית 2 (ירוק) - בין קרן 1 לקרן 2 -->', '<!-- Angle 2 (green) - between ray 1 and ray 2 -->')
    c = r(c, '<!-- זווית 1 (כתום) - בין קרן 2 לצלע AC הימנית -->', '<!-- Angle 1 (orange) - between ray 2 and right side AC -->')
    c = r(c, '<!-- זווית 75° ב-D - זווית חיצונית בין קו AD לקו DE -->', '<!-- 75 degree angle at D - exterior angle between line AD and line DE -->')
    c = r(c, '<!-- D ב-(360, 290), קו AD הולך למעלה-שמאלה, קו DE הולך ימינה -->', '<!-- D at (360, 290), line AD goes up-left, line DE goes right -->')
    c = r(c, '<!-- הזווית היא מימין ל-D, בין הקווים -->', '<!-- The angle is to the right of D, between the lines -->')
    c = r(c, '<!-- תוויות -->', '<!-- Labels -->')

    # More SVG comments
    c = r(c, '<!-- זווית ACD מודגשת - ב-C, בין קו CA לכיוון D -->', '<!-- Angle ACD highlighted - at C, between line CA toward D -->')
    c = r(c, '<!-- זווית 75° -->', '<!-- 75 degree angle -->')
    c = r(c, '<!-- זווית B מודגשת - ב-B בין BA ל-BC -->', '<!-- Angle B highlighted - at B between BA and BC -->')
    c = r(c, '<!-- זווית A כולה (60°) -->', '<!-- Full angle A (60 degrees) -->')
    c = r(c, '<!-- משולש ABC -->', '<!-- Triangle ABC -->')
    c = r(c, '<!-- קו AD -->', '<!-- Line AD -->')
    c = r(c, '<!-- קו BE -->', '<!-- Line BE -->')
    c = r(c, '<!-- זווית A (50°) -->', '<!-- Angle A (50 degrees) -->')
    c = r(c, '<!-- זווית ב-D (70°) + סימון זווית ישרה -->', '<!-- Angle at D (70 degrees) + right angle mark -->')
    c = r(c, '<!-- נקודת F -->', '<!-- Point F -->')
    c = r(c, '<!-- זווית ADB -->', '<!-- Angle ADB -->')
    c = r(c, '<!-- קו EF -->', '<!-- Line EF -->')
    c = r(c, '<!-- זווית EFA -->', '<!-- Angle EFA -->')

    # Per PDF comments
    c = r(c, 'לפי PDF עמוד 2 תרגיל 1:', 'Per PDF page 2 exercise 1:')
    c = r(c, 'A למעלה באמצע, B-C-D-E על הבסיס משמאל לימין', 'A at top center, B-C-D-E on base from left to right')
    c = r(c, 'קודקוד ימני של המשולש הוא בנקודה בין C ל-D (נקרא לה נקודה ימנית)', 'Right vertex of triangle is at point between C and D')
    c = r(c, 'D על הבסיס מימין לקודקוד, קו AD מקווקו', 'D on base to the right of vertex, line AD is dashed')
    c = r(c, "זווית CDE=75° היא זווית חיצונית - בין קו AD לקו DE (לימין)", "Angle CDE=75 degrees is exterior - between line AD and line DE (to the right)")

    # Section headers
    c = r(c, "תרגיל 1 - סעיף א'", "Exercise 1 - Part A")
    c = r(c, "תרגיל 1 - סעיף ב'", "Exercise 1 - Part B")
    c = r(c, "תרגיל 1 - סעיף ג'", "Exercise 1 - Part C")
    c = r(c, "תרגיל 2 - סעיף א'", "Exercise 2 - Part A")
    c = r(c, "תרגיל 2 - סעיף ב'", "Exercise 2 - Part B")
    c = r(c, "תרגיל 2 - סעיף ג'", "Exercise 2 - Part C")
    c = r(c, "תרגיל 2 - סעיף ד'", "Exercise 2 - Part D")

    # Given boxes
    c = r(c, '<div><strong>נתון:</strong> ', '<div><strong>Given:</strong> ')
    c = r(c, '(זווית חיצונית)', '(exterior angle)')
    c = r(c, 'היעזרו בנתונים שבשרטוט וחשבו את הזוויות:', 'Use the data in the diagram to calculate the angles:')
    c = r(c, '<div><strong>ידוע:</strong> ', '<div><strong>Known:</strong> ')
    c = r(c, '(שלוש פעמים 20°)', '(three times 20°)')
    c = r(c, 'AD חוצה את זווית A', 'AD bisects angle A')
    c = r(c, 'BE חוצה את זווית B', 'BE bisects angle B')
    c = r(c, 'F הנקודת חיתוך של AD ו-BE', 'F is the intersection point of AD and BE')
    c = r(c, '(חישבנו בסעיף א)', '(calculated in Part A)')
    c = r(c, '(חישבנו בסעיף ב)', '(calculated in Part B)')
    c = r(c, '(נתון - הוכח בסעיף א)', '(given - proven in Part A)')

    # Question boxes
    c = r(c, 'א. חשבו:', 'A. Calculate:')
    c = r(c, 'ב. חשבו:', 'B. Calculate:')
    c = r(c, 'ג. חשבו:', 'C. Calculate:')
    c = r(c, 'ד. חשבו:', 'D. Calculate:')

    # Feedback hints
    c = r(c, 'רמז: ∠ADE ו-∠CDE הן זוויות סמוכות על ישר. סכומן 180°',
          'Hint: ∠ADE and ∠CDE are supplementary angles on a line. Their sum is 180°')
    c = r(c, 'רמז: משפט הזווית החיצונית - זווית חיצונית = סכום 2 הזוויות הפנימיות שלא צמודות לה',
          'Hint: Exterior angle theorem - exterior angle = sum of 2 non-adjacent interior angles')
    c = r(c, 'רמז: סכום זוויות במשולש = 180°', 'Hint: Sum of angles in a triangle = 180°')
    c = r(c, 'רמז: AD חוצה את זווית A', 'Hint: AD bisects angle A')
    c = r(c, 'רמז: הזווית ∠ADB = 180° - ∠BDC (זוויות משלימות ל-180°)', 'Hint: ∠ADB = 180° - ∠BDC (supplementary angles)')
    c = r(c, 'רמז: BE חוצה את זווית B', 'Hint: BE bisects angle B')
    c = r(c, 'רמז: סכום זוויות במשולש BDF = 180°', 'Hint: Sum of angles in triangle BDF = 180°')

    # Success messages
    c = r(c, '>נכון!<', '>Correct!<')
    c = r(c, '>מצוין!<', '>Excellent!<')
    c = r(c, '>יופי!<', '>Great!<')
    c = r(c, '>נכון!</', '>Correct!</')
    c = r(c, '>כל הכבוד!<', '>Well done!<')
    c = r(c, '>מדויק!<', '>Exactly!<')
    c = r(c, '>בול!<', '>Spot on!<')

    # Explanations
    c = r(c, '<strong>פתרון:</strong>', '<strong>Solution:</strong>')
    c = r(c, '(זוויות סמוכות)', '(supplementary angles)')
    c = r(c, '<strong>משפט הזווית החיצונית:</strong>', '<strong>Exterior Angle Theorem:</strong>')
    c = r(c, '<strong>סכום זוויות במשולש:</strong>', '<strong>Sum of angles in a triangle:</strong>')
    c = r(c, '<strong>חוצה זווית:</strong>', '<strong>Angle bisector:</strong>')
    c = r(c, '(חוצה זווית)', '(angle bisector)')
    c = r(c, '(AD חוצה את A)', '(AD bisects A)')
    c = r(c, '<strong>זוויות משלימות:</strong>', '<strong>Supplementary angles:</strong>')
    c = r(c, '(זוויות משלימות ל-180°)', '(supplementary to 180°)')
    c = r(c, 'BE חוצה את B →', 'BE bisects B →')
    c = r(c, '<strong>סכום זוויות במשולש BDF:</strong>', '<strong>Sum of angles in triangle BDF:</strong>')

    # Continue buttons
    c = r(c, "לסעיף ב'", "To Part B")
    c = r(c, "לסעיף ג'", "To Part C")
    c = r(c, 'לתרגיל 2', 'To Exercise 2')
    c = r(c, "לסעיף ד'", "To Part D")
    c = r(c, 'לסיכום', 'To Summary')

    # Summary page
    c = r(c, 'כל הכבוד! סיימת את עמוד 2', 'Well done! You completed Page 2')
    c = r(c, 'סיכום התשובות:', 'Summary of Answers:')
    c = r(c, 'סיימת', 'Completed')

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page2.html', c)
    print('page2.html translated')

# ============================================================
# page2_q4_parallel.html
# ============================================================
def translate_page2_q4():
    c = read_file('page2_q4_parallel.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')
    c = r(c, 'שאלה 4 - ישרים מקבילים', 'Question 4 - Parallel Lines')

    # RTL layout fixes
    c = r(c, 'text-align: right;', 'text-align: left;')
    c = r(c, 'margin-left: 10px;', 'margin-right: 10px;')

    # Title and exercise
    c = r(c, '>ישרים מקבילים<', '>Parallel Lines<')
    c = r(c, 'שאלה 4 - מצאו את הישרים המקבילים', 'Question 4 - Find the Parallel Lines')
    c = r(c, 'alt="שרטוט ישרים מקבילים"', 'alt="Parallel lines diagram"')

    # Given box
    c = r(c, '<div><strong>נתון - הזוויות המסומנות בשרטוט:</strong></div>', '<div><strong>Given - The angles marked in the diagram:</strong></div>')
    c = r(c, 'ישר <b>a</b> עם חותך <b>e</b>:', 'Line <b>a</b> with transversal <b>e</b>:')
    c = r(c, 'ישר <b>c</b> עם חותך <b>e</b>:', 'Line <b>c</b> with transversal <b>e</b>:')
    c = r(c, 'ישר <b>d</b> עם חותך <b>f</b>:', 'Line <b>d</b> with transversal <b>f</b>:')
    c = r(c, 'ישר <b>c</b> עם חותך <b>f</b>:', 'Line <b>c</b> with transversal <b>f</b>:')

    # Info box (reminder)
    c = r(c, '<h4>תזכורת - מתי ישרים מקבילים?</h4>', '<h4>Reminder - When are lines parallel?</h4>')
    c = r(c, 'זוויות חד-צדדיות פנימיות שסכומן <b>180°</b> → ישרים מקבילים',
          'Co-interior angles (same-side interior) that sum to <b>180°</b> → parallel lines')
    c = r(c, 'זוויות מתאימות שוות → ישרים מקבילים', 'Corresponding angles are equal → parallel lines')
    c = r(c, 'זוויות מתחלפות שוות → ישרים מקבילים', 'Alternate angles are equal → parallel lines')

    # Comments
    c = r(c, '<!-- שאלה א - ישרים אופקיים מקבילים -->', '<!-- Question A - Horizontal parallel lines -->')
    c = r(c, '<!-- שאלה ב - ישרים אלכסוניים מקבילים -->', '<!-- Question B - Diagonal parallel lines -->')
    c = r(c, '<!-- סיכום -->', '<!-- Summary -->')

    # Question labels
    c = r(c, 'א. מצאו את הישרים האופקיים המקבילים:', 'A. Find the horizontal parallel lines:')
    c = r(c, 'ב. מצאו את הישרים האלכסוניים (החותכים) המקבילים:', 'B. Find the diagonal (transversal) parallel lines:')

    # Hints
    c = r(c, 'רמז: בדקו אילו ישרים יוצרים זוויות חד-צדדיות שסכומן 180°',
          'Hint: Check which lines form co-interior angles that sum to 180°')
    c = r(c, 'רמז: בדקו את הזוויות שהישרים e ו-f יוצרים עם ישר c',
          'Hint: Check the angles that lines e and f form with line c')

    # Answer rows
    c = r(c, 'הישרים המקבילים הם:', 'The parallel lines are:')
    c = r(c, 'placeholder="לדוגמה: a,c,d"', 'placeholder="e.g.: a,c,d"')
    c = r(c, 'placeholder="לדוגמה: e,f"', 'placeholder="e.g.: e,f"')
    c = r(c, '>בדוק<', '>Check<')

    # Success
    c = r(c, '✓ נכון!', '✓ Correct!')

    # Explanations
    c = r(c, '<strong>הסבר:</strong>', '<strong>Explanation:</strong>')
    c = r(c, 'ישר <b>a</b> עם ישר <b>c</b>:', 'Line <b>a</b> with line <b>c</b>:')
    c = r(c, 'ישר <b>c</b> עם ישר <b>d</b>:', 'Line <b>c</b> with line <b>d</b>:')
    c = r(c, 'ישר <b>e</b> יוצר עם <b>c</b> זווית', 'Line <b>e</b> forms with <b>c</b> an angle of')
    c = r(c, 'ישר <b>f</b> יוצר עם <b>c</b> זווית', 'Line <b>f</b> forms with <b>c</b> an angle of')
    c = r(c, '• לכן: <b>a ∥ c ∥ d</b>', '• Therefore: <b>a ∥ c ∥ d</b>')

    # Summary
    c = r(c, 'סיכום - כל הישרים המקבילים:', 'Summary - All Parallel Lines:')

    # JS hints
    c = r(c, "'בדקו: 70° + 110° = ?'", "'Check: 70° + 110° = ?'")
    c = r(c, "'אם הסכום הוא 180°, הישרים מקבילים!'", "'If the sum is 180°, the lines are parallel!'")
    c = r(c, "'הישרים a, c, d - בדקו את הזוויות ביניהם'", "'Lines a, c, d - check the angles between them'")
    c = r(c, "'הסתכלו על הזוויות של e ו-f עם ישר c'", "'Look at the angles of e and f with line c'")
    c = r(c, "'110° + 70° = 180° - מה זה אומר?'", "'110° + 70° = 180° - what does this mean?'")
    c = r(c, "'e ו-f הם החותכים - האם הם מקבילים?'", "'e and f are the transversals - are they parallel?'")

    # JS hint text
    c = r(c, "רמז ", "Hint ")
    c = r(c, "התשובה:", "The answer:")

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page2_q4_parallel.html', c)
    print('page2_q4_parallel.html translated')

# ============================================================
# page3.html - Equations and Inequalities
# ============================================================
def translate_page3():
    c = read_file('page3.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')
    c = r(c, 'משוואות ואי-שוויונות - פתרון מודרך', 'Equations and Inequalities - Guided Solution')

    # RTL layout fixes
    c = r(c, 'text-align: right;', 'text-align: left;')

    # Header
    c = r(c, '>משוואות ואי-שוויונות<', '>Equations and Inequalities<')

    # Progress text
    c = r(c, "' תרגיל '", "' Exercise '")
    c = r(c, "' מתוך '", "' of '")

    # Exercise titles
    c = r(c, 'פתרו משוואה', 'Solve the equation')
    c = r(c, 'פתרו אי-שוויון', 'Solve the inequality')

    # Step titles
    c = r(c, 'פתיחת סוגריים', 'Expand brackets')
    c = r(c, 'צמצום איברים דומים', 'Combine like terms')
    c = r(c, 'העברת אגפים', 'Rearrange sides')
    c = r(c, 'חילוק', 'Division')
    c = r(c, 'בדיקה', 'Verification')
    c = r(c, 'התשובה', 'The answer')
    c = r(c, 'כפל צולב', 'Cross multiplication')
    c = r(c, 'איסוף איברים', 'Collecting terms')
    c = r(c, 'חילוק ב-', 'Divide by ')
    c = r(c, 'חילוק במספר שלילי', 'Division by a negative number')

    # Question texts
    c = r(c, 'מהו הפתרון?', 'What is the solution?')
    c = r(c, 'מהו הפתרון של אי-השוויון?', 'What is the solution of the inequality?')

    # Explanations in steps
    c = r(c, '(נפתח את הסוגריים)', '(expand the brackets)')
    c = r(c, '(נצמצם)', '(simplify)')
    c = r(c, '(נעביר אגפים)', '(rearrange)')
    c = r(c, '(נחלק ב-', '(divide by ')
    c = r(c, '(נפתח סוגריים)', '(expand brackets)')
    c = r(c, '(כפל צולב)', '(cross multiply)')
    c = r(c, '(נאסוף איברים דומים)', '(collect like terms)')

    # Important note about inequality
    c = r(c, 'שימו לב! כשמחלקים במספר שלילי, הכיוון מתהפך!',
          'Note! When dividing by a negative number, the inequality sign flips!')
    c = r(c, 'כשמחלקים/כופלים במספר שלילי → מהפכים כיוון!',
          'When dividing/multiplying by a negative number → flip the sign!')

    # Buttons
    c = r(c, 'הצג שלב הבא', 'Show Next Step')
    c = r(c, 'תרגיל הבא', 'Next Exercise')
    c = r(c, 'חזרה להתחלה', 'Back to Start')

    # Final/success messages
    c = r(c, 'כל הכבוד!', 'Well done!')
    c = r(c, 'סיימת את כל התרגילים!', 'You completed all the exercises!')
    c = r(c, "'מעולה! '", "'Excellent! '")
    c = r(c, "'נכון!'", "'Correct!'")
    c = r(c, "'לא נכון, נסו שוב'", "'Incorrect, try again'")

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page3.html', c)
    print('page3.html translated')

# ============================================================
# page4.html - Gardeners pricing graph literacy
# ============================================================
def translate_page4():
    c = read_file('page4.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')
    c = r(c, 'עמוד 4: הצעות הגננים - אוריינות גרפית', 'Page 4: Gardener Proposals - Graph Literacy')

    # RTL layout fixes - gardener card border
    c = r(c, 'border-right: 4px solid;', 'border-left: 4px solid;')
    c = r(c, 'border-right-color: var(--orange);', 'border-left-color: var(--orange);')
    c = r(c, 'border-right-color: var(--teal);', 'border-left-color: var(--teal);')
    c = r(c, 'border-right: 3px solid var(--purple);', 'border-left: 3px solid var(--purple);')

    # Title
    c = r(c, '>הצעות הגננים - אוריינות גרפית<', '>Gardener Proposals - Graph Literacy<')

    # Problem statement
    c = r(c, '<h3>הבעיה:</h3>', '<h3>The Problem:</h3>')
    c = r(c, 'אורן ותומר הם גננים. כל אחד מהם פרסם באתר השכונתי הצעת מחיר בעבור ייעוץ וטיפול בגינה.',
          'Oren and Tomer are gardeners. Each of them posted a price proposal on the neighborhood website for consultation and garden maintenance.')

    # Gardener cards
    c = r(c, '>אורן<', '>Oren<')
    c = r(c, '>תומר<', '>Tomer<')
    c = r(c, '700 שקלים לייעוץ ועוד 20 שקלים לגינון של כל מ"ר גינה',
          '700 shekels for consultation plus 20 shekels per sq. meter of garden')
    c = r(c, '48 שקלים לכל מ"ר גינה (הייעוץ כלול במחיר)',
          '48 shekels per sq. meter of garden (consultation included)')

    # Graph
    c = r(c, '>גרף המחירים לפי שטח הגינה<', '>Price Graph by Garden Area<')
    c = r(c, 'שטח הגינה (מ"ר)', 'Garden Area (sq. m)')
    c = r(c, 'מחיר (שקלים)', 'Price (shekels)')
    c = r(c, '816 ש"ח', '816 NIS')
    c = r(c, '1040 ש"ח', '1040 NIS')

    # Legend
    c = r(c, 'גרף I - אורן', 'Graph I - Oren')
    c = r(c, 'גרף II - תומר', 'Graph II - Tomer')

    # Questions
    c = r(c, 'א. איזה גרף, I או II, מתאר את ההצעה של אורן?', 'A. Which graph, I or II, describes Oren\'s proposal?')
    c = r(c, '>גרף I<', '>Graph I<')
    c = r(c, '>גרף II<', '>Graph II<')
    c = r(c, '>שניהם<', '>Both<')
    c = r(c, '>אף אחד מהם<', '>Neither<')

    c = r(c, 'ב. (1) מהו שטח הגינה שבעבורו הגננים אורן ותומר גובים את אותו המחיר?',
          'B. (1) What is the garden area for which gardeners Oren and Tomer charge the same price?')
    c = r(c, '20 מ"ר', '20 sq. m')
    c = r(c, '25 מ"ר', '25 sq. m')
    c = r(c, '30 מ"ר', '30 sq. m')
    c = r(c, '35 מ"ר', '35 sq. m')

    c = r(c, 'ב. (2) מהו המחיר בעבור השטח הזה?', 'B. (2) What is the price for that area?')
    c = r(c, '1,000 שקלים', '1,000 shekels')
    c = r(c, '1,100 שקלים', '1,100 shekels')
    c = r(c, '1,200 שקלים', '1,200 shekels')
    c = r(c, '1,400 שקלים', '1,400 shekels')

    # Context
    c = r(c, 'למשפחת כהן יש גינה ששטחה 17 מ"ר. משפחת כהן בחרה בגנן שהצעת המחיר שלו הייתה נמוכה יותר.',
          'The Cohen family has a garden with an area of 17 sq. m. The Cohen family chose the gardener whose price proposal was lower.')

    c = r(c, '(1) במי משני הגננים בחרה משפחת כהן?', '(1) Which of the two gardeners did the Cohen family choose?')
    c = r(c, '>אורן<', '>Oren<')
    c = r(c, '>תומר<', '>Tomer<')
    c = r(c, '>אותו מחיר לשניהם<', '>Same price for both<')
    c = r(c, '>אי אפשר לדעת<', '>Cannot be determined<')

    c = r(c, '(2) מצאו בכמה שקלים הייתה גבוהה הצעת המחיר של הגנן האחר מן המחיר ששילמה משפחת כהן.',
          "(2) Find by how many shekels the other gardener's price proposal was higher than the price the Cohen family paid.")
    c = r(c, '124 שקלים', '124 shekels')
    c = r(c, '200 שקלים', '200 shekels')
    c = r(c, '224 שקלים', '224 shekels')
    c = r(c, '324 שקלים', '324 shekels')

    # Score/feedback
    c = r(c, 'כל הכבוד! סיימת את כל השאלות', 'Well done! You completed all the questions')
    c = r(c, 'התחל מחדש', 'Start Over')

    # JS feedback texts
    c = r(c, "נכון! גרף I מתחיל ב-700 ועולה לאט", "Correct! Graph I starts at 700 and rises slowly")
    c = r(c, "לא. גרף II מתחיל מ-0 - זה תומר", "No. Graph II starts from 0 - that's Tomer")
    c = r(c, "לא. כל גרף מתאר גנן אחד", "No. Each graph describes one gardener")
    c = r(c, "לא. גרף I מתאר את אורן", "No. Graph I describes Oren")

    c = r(c, 'לא. ב-20 מ\\"ר הגרפים לא נחתכים', "No. At 20 sq. m the graphs don't intersect")
    c = r(c, 'נכון! נקודת החיתוך: 700+20x=48x → x=25', 'Correct! Intersection point: 700+20x=48x → x=25')
    c = r(c, 'לא. ב-30 מ\\"ר המחירים שונים', 'No. At 30 sq. m the prices differ')
    c = r(c, 'לא. ב-35 מ\\"ר כבר עברנו את החיתוך', "No. At 35 sq. m we've already passed the intersection")

    c = r(c, 'לא. חשב: 48×25 או 700+20×25', 'No. Calculate: 48×25 or 700+20×25')
    c = r(c, 'לא. המחיר גבוה יותר', 'No. The price is higher')
    c = r(c, 'נכון! 48×25 = 1,200 שקלים', 'Correct! 48×25 = 1,200 shekels')
    c = r(c, 'לא. זה יותר מדי', "No. That's too much")

    c = r(c, 'לא. אורן גובה 1,040 ש\\"ח - יקר יותר!', 'No. Oren charges 1,040 NIS - more expensive!')
    c = r(c, 'נכון! תומר גובה רק 816 ש\\"ח', 'Correct! Tomer charges only 816 NIS')
    c = r(c, 'לא. 816 ≠ 1,040', 'No. 816 ≠ 1,040')
    c = r(c, 'לא. אפשר לחשב מהגרף', 'No. It can be calculated from the graph')

    c = r(c, 'לא. חשב: 1,040 - 816', 'No. Calculate: 1,040 - 816')
    c = r(c, 'לא. ההפרש גדול יותר', 'No. The difference is larger')
    c = r(c, 'נכון! 1,040 - 816 = 224', 'Correct! 1,040 - 816 = 224')
    c = r(c, 'לא. זה יותר מדי', "No. That's too much")

    # Try again
    c = r(c, ' נסה שוב!', ' Try again!')

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page4.html', c)
    print('page4.html translated')

# ============================================================
# page4_q5_pricing.html
# ============================================================
def translate_page4_q5():
    c = read_file('page4_q5_pricing.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')
    c = r(c, 'גרפים של מחירים - אורן ותומר', 'Price Graphs - Oren and Tomer')

    # RTL layout fixes
    c = r(c, 'text-align: right;', 'text-align: left;')

    # Title/subtitle
    c = r(c, '>הצעות הגננים - אוריינות גרפית<', '>Gardener Proposals - Graph Literacy<')
    c = r(c, '>שאלה 5 - ניתוח הגרפים<', '>Question 5 - Graph Analysis<')

    # Given box
    c = r(c, '<strong>תזכורת - הנתונים:</strong>', '<strong>Reminder - The Data:</strong>')
    c = r(c, 'אורן:', 'Oren:')
    c = r(c, '700 שקלים לייעוץ + 20 שקלים למ"ר', '700 shekels for consultation + 20 shekels per sq. m')
    c = r(c, 'תומר:', 'Tomer:')
    c = r(c, '48 שקלים למ"ר (כולל ייעוץ)', '48 shekels per sq. m (including consultation)')

    # Graph labels
    c = r(c, 'שטח הגינה (מ"ר)', 'Garden Area (sq. m)')
    c = r(c, 'מחיר (שקלים)', 'Price (shekels)')
    c = r(c, 'גרף I - אורן (y = 700 + 20x)', 'Graph I - Oren (y = 700 + 20x)')
    c = r(c, 'גרף II - תומר (y = 48x)', 'Graph II - Tomer (y = 48x)')

    # Questions
    c = r(c, 'א. מצאו את נקודת החיתוך של שני הגרפים', 'A. Find the intersection point of the two graphs')
    c = r(c, 'ב. מה קורה כשהגינה קטנה מ-25 מ"ר?', 'B. What happens when the garden is smaller than 25 sq. m?')
    c = r(c, 'ג. מה קורה כשהגינה גדולה מ-25 מ"ר?', 'C. What happens when the garden is larger than 25 sq. m?')

    # Options
    c = r(c, 'תומר זול יותר', 'Tomer is cheaper')
    c = r(c, 'אורן זול יותר', 'Oren is cheaper')
    c = r(c, 'אותו מחיר', 'Same price')
    c = r(c, 'אי אפשר לדעת', 'Cannot be determined')

    # Sub-questions about intersection
    c = r(c, 'שטח הגינה בנקודת החיתוך:', 'Garden area at intersection:')
    c = r(c, 'המחיר בנקודת החיתוך:', 'Price at intersection:')

    # Answer options for intersection
    c = r(c, '20 מ"ר', '20 sq. m')
    c = r(c, '25 מ"ר', '25 sq. m')
    c = r(c, '30 מ"ר', '30 sq. m')
    c = r(c, '15 מ"ר', '15 sq. m')

    # Price options
    c = r(c, '1,000 ₪', '1,000 NIS')
    c = r(c, '1,200 ₪', '1,200 NIS')
    c = r(c, '1,400 ₪', '1,400 NIS')
    c = r(c, '960 ₪', '960 NIS')

    # Feedback
    c = r(c, 'נכון!', 'Correct!')
    c = r(c, 'לא נכון, נסו שוב', 'Incorrect, try again')
    c = r(c, 'לא נכון.', 'Incorrect.')

    # Explanations
    c = r(c, 'הגרפים נחתכים כש:', 'The graphs intersect when:')
    c = r(c, 'בנקודת החיתוך שני הגננים גובים אותו מחיר:', 'At the intersection both gardeners charge the same price:')
    c = r(c, 'כשהגינה קטנה מ-25 מ"ר, גרף II (תומר) נמצא מתחת לגרף I (אורן)',
          'When the garden is smaller than 25 sq. m, Graph II (Tomer) is below Graph I (Oren)')
    c = r(c, 'כשהגינה גדולה מ-25 מ"ר, גרף I (אורן) נמצא מתחת לגרף II (תומר)',
          'When the garden is larger than 25 sq. m, Graph I (Oren) is below Graph II (Tomer)')

    # Summary
    c = r(c, 'כל הכבוד! סיימת את השאלה', 'Well done! You completed the question')
    c = r(c, 'סיכום:', 'Summary:')
    c = r(c, 'נקודת החיתוך:', 'Intersection point:')
    c = r(c, 'עד 25 מ"ר - תומר זול יותר', 'Up to 25 sq. m - Tomer is cheaper')
    c = r(c, 'מעל 25 מ"ר - אורן זול יותר', 'Above 25 sq. m - Oren is cheaper')
    c = r(c, 'התחל מחדש', 'Start Over')

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page4_q5_pricing.html', c)
    print('page4_q5_pricing.html translated')

# ============================================================
# page5.html - Functions - Truck from Haifa
# ============================================================
def translate_page5():
    c = read_file('page5.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')
    c = r(c, 'עמוד 5: פונקציות - משאית מחיפה', 'Page 5: Functions - Truck from Haifa')

    # Title
    c = r(c, '>פונקציות - משאית מחיפה<', '>Functions - Truck from Haifa<')

    # Problem description
    c = r(c, 'משאית נוסעת מחיפה דרומה.', 'A truck travels south from Haifa.')
    c = r(c, 'הגרף מתאר את המרחק של המשאית מחיפה (בק"מ) כפונקציה של הזמן (בשעות) מתחילת הנסיעה.',
          'The graph describes the distance of the truck from Haifa (in km) as a function of time (in hours) from the start of the trip.')

    # Graph
    c = r(c, '>גרף המרחק-זמן של המשאית<', '>Distance-Time Graph of the Truck<')
    c = r(c, 'זמן (שעות)', 'Time (hours)')
    c = r(c, 'מרחק מחיפה (ק"מ)', 'Distance from Haifa (km)')

    # Questions
    c = r(c, 'מהו המרחק מחיפה לאחר שעתיים?', 'What is the distance from Haifa after 2 hours?')
    c = r(c, 'כמה זמן עצרה המשאית?', 'How long did the truck stop?')
    c = r(c, 'מהי המהירות הממוצעת ב-2 השעות הראשונות?', 'What is the average speed in the first 2 hours?')
    c = r(c, 'באיזה קטע המשאית נסעה הכי מהר?', 'In which segment did the truck travel the fastest?')
    c = r(c, 'מהו סך כל המרחק שהמשאית עברה?', 'What is the total distance the truck traveled?')

    # Answer options
    c = r(c, 'ק"מ', 'km')
    c = r(c, 'שעה אחת', 'One hour')
    c = r(c, 'שעתיים', 'Two hours')
    c = r(c, 'חצי שעה', 'Half an hour')
    c = r(c, 'שעה וחצי', 'An hour and a half')
    c = r(c, 'קמ"ש', 'km/h')
    c = r(c, 'הקטע הראשון (0-2)', 'First segment (0-2)')
    c = r(c, 'הקטע השלישי (3-4.5)', 'Third segment (3-4.5)')
    c = r(c, 'הקטע הרביעי (4.5-5)', 'Fourth segment (4.5-5)')
    c = r(c, 'הקטע השני (2-3)', 'Second segment (2-3)')

    # Feedback
    c = r(c, 'נכון!', 'Correct!')
    c = r(c, 'לא נכון.', 'Incorrect.')
    c = r(c, 'נסו שוב', 'Try again')

    # Explanations
    c = r(c, 'מהגרף: לאחר 2 שעות, המשאית נמצאת במרחק 120 ק"מ מחיפה',
          'From the graph: after 2 hours, the truck is 120 km from Haifa')
    c = r(c, 'המשאית עצרה בין שעה 2 לשעה 3 (הגרף שטוח) - סה"כ שעה אחת',
          'The truck stopped between hour 2 and hour 3 (graph is flat) - total of one hour')
    c = r(c, 'מהירות = מרחק / זמן = 120 / 2 = 60 קמ"ש',
          'Speed = distance / time = 120 / 2 = 60 km/h')
    c = r(c, 'בקטע 4.5-5 המשאית עברה 60 ק"מ בחצי שעה = 120 קמ"ש',
          'In segment 4.5-5 the truck traveled 60 km in half an hour = 120 km/h')
    c = r(c, 'מהגרף: המשאית הגיעה למרחק 300 ק"מ מחיפה',
          'From the graph: the truck reached 300 km from Haifa')

    # Score
    c = r(c, 'כל הכבוד! סיימת את כל השאלות', 'Well done! You completed all the questions')
    c = r(c, 'התחל מחדש', 'Start Over')

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page5.html', c)
    print('page5.html translated')

# ============================================================
# page5_q6a_table.html
# ============================================================
def translate_page5_q6a():
    c = read_file('page5_q6a_table.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')

    # Title
    c = r(c, 'שאלה 6א - טבלת ערכים', 'Question 6A - Value Table')

    # RTL fixes
    c = r(c, 'text-align: right;', 'text-align: left;')

    # Content
    c = r(c, 'טבלת ערכים - חנות הפלאפל', 'Value Table - Falafel Shop')
    c = r(c, '>שאלה 6<', '>Question 6<')
    c = r(c, 'חנות פלאפל מוכרת מנות פלאפל.', 'A falafel shop sells falafel portions.')
    c = r(c, 'מחיר מנה:', 'Price per portion:')
    c = r(c, 'שקלים למנה', 'shekels per portion')
    c = r(c, 'הוצאות קבועות של החנות:', 'Fixed expenses of the shop:')
    c = r(c, 'שקלים ביום', 'shekels per day')
    c = r(c, 'פונקציית הרווח:', 'Profit function:')
    c = r(c, 'כאשר x = מספר המנות שנמכרו', 'where x = number of portions sold')

    # Table
    c = r(c, 'מספר מנות (x)', 'Number of portions (x)')
    c = r(c, 'רווח y (שקלים)', 'Profit y (shekels)')
    c = r(c, 'מלאו את הטבלה:', 'Fill in the table:')
    c = r(c, 'בדוק הכל', 'Check All')

    # Feedback
    c = r(c, 'נכון!', 'Correct!')
    c = r(c, 'נסו שוב', 'Try again')
    c = r(c, 'לא נכון', 'Incorrect')
    c = r(c, 'מצוין! כל התשובות נכונות!', 'Excellent! All answers are correct!')
    c = r(c, 'יש טעויות. נסו לתקן', 'There are errors. Try to fix them')

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page5_q6a_table.html', c)
    print('page5_q6a_table.html translated')

# ============================================================
# page5_q6bcdef_analysis.html
# ============================================================
def translate_page5_q6bcdef():
    c = read_file('page5_q6bcdef_analysis.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')

    # Title
    c = r(c, 'שאלה 6 - ניתוח פונקציית הרווח', 'Question 6 - Profit Function Analysis')

    # RTL fixes
    c = r(c, 'text-align: right;', 'text-align: left;')
    c = r(c, 'border-right: 3px solid', 'border-left: 3px solid')

    # Content
    c = r(c, 'ניתוח פונקציית הרווח', 'Profit Function Analysis')
    c = r(c, 'חנות הפלאפל', 'Falafel Shop')
    c = r(c, 'פונקציית רווח:', 'Profit function:')
    c = r(c, 'מספר מנות (x)', 'Number of portions (x)')
    c = r(c, 'רווח (שקלים)', 'Profit (shekels)')

    # Questions
    c = r(c, 'ב. מהו שיפוע הגרף ומה משמעותו?', 'B. What is the slope of the graph and what does it mean?')
    c = r(c, 'ג. מהו ערך ה-y כאשר x=0 ומה משמעותו?', 'C. What is the y-value when x=0 and what does it mean?')
    c = r(c, 'ד. באיזה ערך x החנות מתחילה להרוויח?', 'D. At which x value does the shop start making a profit?')
    c = r(c, 'ה. מהו הרווח ממכירת 40 מנות?', 'E. What is the profit from selling 40 portions?')
    c = r(c, 'ו. כמה מנות צריך למכור כדי להרוויח 200 שקלים?', 'F. How many portions need to be sold to earn 200 shekels?')

    # Options and answers
    c = r(c, 'שקלים למנה - הרווח מכל מנה', 'shekels per portion - profit per portion')
    c = r(c, 'מנות - נקודת האיזון', 'portions - break-even point')
    c = r(c, 'שקלים - ההוצאות הקבועות (הפסד בלי מכירות)', 'shekels - fixed expenses (loss without sales)')
    c = r(c, 'שקלים', 'shekels')
    c = r(c, 'מנות', 'portions')

    # Feedback
    c = r(c, 'נכון!', 'Correct!')
    c = r(c, 'לא נכון', 'Incorrect')
    c = r(c, 'נסו שוב', 'Try again')
    c = r(c, 'כל הכבוד!', 'Well done!')

    # Explanations
    c = r(c, 'השיפוע הוא 12 - כל מנה מוסיפה 12 שקלים לרווח', 'The slope is 12 - each portion adds 12 shekels to profit')
    c = r(c, 'כש-x=0 הרווח הוא -180 שקלים - ההפסד מההוצאות הקבועות', 'When x=0 the profit is -180 shekels - the loss from fixed expenses')
    c = r(c, 'נקודת האיזון: 12x - 180 = 0 → x = 15 מנות', 'Break-even point: 12x - 180 = 0 → x = 15 portions')
    c = r(c, 'y = 12(40) - 180 = 480 - 180 = 300 שקלים', 'y = 12(40) - 180 = 480 - 180 = 300 shekels')
    c = r(c, '200 = 12x - 180 → 12x = 380 → x ≈ 32 מנות', '200 = 12x - 180 → 12x = 380 → x ≈ 32 portions')

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page5_q6bcdef_analysis.html', c)
    print('page5_q6bcdef_analysis.html translated')

# ============================================================
# page6.html
# ============================================================
def translate_page6():
    c = read_file('page6.html')

    c = r(c, 'lang="he" dir="rtl"', 'lang="en" dir="ltr"')

    # RTL fixes
    c = r(c, 'text-align: right;', 'text-align: left;')

    # Title and common patterns first
    # Then grep remaining Hebrew and fix

    # All Hebrew patterns in page6
    c = r(c, 'עמוד 6', 'Page 6')
    c = r(c, 'סיכום ותרגול', 'Summary and Practice')
    c = r(c, 'שאלות סיכום', 'Summary Questions')
    c = r(c, 'כל הכבוד!', 'Well done!')
    c = r(c, 'סיימת', 'You finished')
    c = r(c, 'התחל מחדש', 'Start Over')
    c = r(c, 'נכון!', 'Correct!')
    c = r(c, 'לא נכון', 'Incorrect')
    c = r(c, 'נסו שוב', 'Try again')

    # Footer
    c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

    write_file('page6.html', c)
    print('page6.html translated')

# Run all translations
translate_index()
translate_page2()
translate_page2_q4()
translate_page3()
translate_page4()
translate_page4_q5()
translate_page5()
translate_page5_q6a()
translate_page5_q6bcdef()
translate_page6()

print("\n=== DONE ===")
