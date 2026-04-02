#!/usr/bin/env python3
"""Second pass translation - catch all remaining Hebrew."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

def read_file(name):
    with open(os.path.join(BASE, name), 'r', encoding='utf-8') as f:
        return f.read()

def write_file(name, content):
    with open(os.path.join(BASE, name), 'w', encoding='utf-8') as f:
        f.write(content)

def r(c, old, new):
    return c.replace(old, new)

# ============================================================
# index.html - remaining
# ============================================================
c = read_file('index.html')
c = r(c, 'כבר הוכחנו בQuadrilateral ABCD:', 'Already proven in Quadrilateral ABCD:')
c = r(c, 'בQuadrilateral ABCD:', 'In Quadrilateral ABCD:')
c = r(c, 'בQuadrilateral EFGH:', 'In Quadrilateral EFGH:')
c = r(c, 'כל החפיפות היו by SAS - בזכות הזוויות הקודקודיות!', 'All congruences were by SAS - thanks to vertical angles!')
write_file('index.html', c)
print('index.html pass2 done')

# ============================================================
# page4.html - remaining
# ============================================================
c = read_file('page4.html')
c = r(c, '<strong style="color: #a78bfa;">ג.</strong>', '<strong style="color: #a78bfa;">C.</strong>')
c = r(c, '"נכון! 48×25 = 1,200 shekels"', '"Correct! 48×25 = 1,200 shekels"')
write_file('page4.html', c)
print('page4.html pass2 done')

# ============================================================
# page2.html - lots remaining
# ============================================================
c = read_file('page2.html')

# Given items
c = r(c, '(הזווית המסומנת "1")', '(the angle marked "1")')
c = r(c, 'זווית חיצונית של △ACD', 'exterior angle of △ACD')

# Feedback hints remaining
c = r(c, 'רמז: AD bisects angle A', 'Hint: AD bisects angle A')
c = r(c, 'AD חוצה את ∠A:', 'AD bisects ∠A:')
c = r(c, '<!-- הדגשת זווית ABE -->', '<!-- Highlight angle ABE -->')
c = r(c, 'רמז: סכום זוויות במשולש ABD', 'Hint: Sum of angles in triangle ABD')
c = r(c, '>מעולה!</', '>Excellent!</')
c = r(c, '>מעולה!<', '>Excellent!<')
c = r(c, 'במשולש ABD:', 'In triangle ABD:')
c = r(c, '<!-- הדגשת זווית BFD -->', '<!-- Highlight angle BFD -->')
c = r(c, '<div><strong>F</strong> היא נקודת החיתוך של AD ו-BE', '<div><strong>F</strong> is the intersection point of AD and BE')
c = r(c, 'רמז: סכום זוויות במשולש BFD', 'Hint: Sum of angles in triangle BFD')
c = r(c, 'במשולש BFD:', 'In triangle BFD:')
c = r(c, '<!-- הדגשת זווית DFE -->', '<!-- Highlight angle DFE -->')
c = r(c, 'רמז: ∠BFD ו-∠DFE הן זוויות סמוכות', 'Hint: ∠BFD and ∠DFE are supplementary angles')
c = r(c, '>לתרגיל 3<', '>To Exercise 3<')

# Exercise 3
c = r(c, '<!-- ==================== תרגיל 3 סעיף א ====================', '<!-- ==================== Exercise 3 Part A ====================')
c = r(c, "תרגיל 3 - משולש שווה-שוקיים - סעיף א'", 'Exercise 3 - Isosceles Triangle - Part A')
c = r(c, '<!-- המשך BA מעל A (ל-D) -->', '<!-- Extension of BA above A (to D) -->')
c = r(c, '<!-- צלעות המשולש -->', '<!-- Triangle sides -->')
c = r(c, '<!-- קו AK -->', '<!-- Line AK -->')
c = r(c, '<!-- סימוני צלעות שוות -->', '<!-- Equal sides marks -->')
c = r(c, '<!-- זווית בסיס B (64°) -->', '<!-- Base angle B (64 degrees) -->')
c = r(c, '<!-- זווית בסיס C (64°) -->', '<!-- Base angle C (64 degrees) -->')
c = r(c, '△ABC משולש שווה-שוקיים (AB = AC)', '△ABC is an isosceles triangle (AB = AC)')
c = r(c, 'גודל זווית בסיס של המשולש 64°', 'The base angle of the triangle is 64°')
c = r(c, 'AK חוצה את ∠DAC', 'AK bisects ∠DAC')
c = r(c, 'א. חשבו את גדלי כל הזוויות - מהי זווית הראש?', 'A. Calculate all the angles - what is the apex angle?')

# Exercise 3 Part B
c = r(c, '<!-- ==================== תרגיל 3 סעיף ב ====================', '<!-- ==================== Exercise 3 Part B ====================')
c = r(c, "תרגיל 3 - סעיף ב' - הוכחה", "Exercise 3 - Part B - Proof")
c = r(c, '<!-- BC מודגש -->', '<!-- BC highlighted -->')
c = r(c, '<!-- AK מודגש -->', '<!-- AK highlighted -->')
c = r(c, '<!-- זווית KAC = 64° -->', '<!-- Angle KAC = 64 degrees -->')
c = r(c, '<!-- זווית ACB = 64° -->', '<!-- Angle ACB = 64 degrees -->')
c = r(c, '<div><strong>ידוע:</strong></div>', '<div><strong>Known:</strong></div>')
c = r(c, '(AK חוצה)', '(AK bisects)')
c = r(c, 'ב. מדוע BC || AK?', 'B. Why is BC || AK?')
c = r(c, 'זוויות מתחלפות שוות', 'Equal alternate angles')
c = r(c, 'זוויות צמודות', 'Adjacent angles')
c = r(c, 'זוויות קודקודיות', 'Vertical angles')
c = r(c, 'זוויות מתאימות', 'Corresponding angles')
c = r(c, 'רמז: ∠KAC ו-∠ACB נמצאות בצדדים מנוגדים של AC', 'Hint: ∠KAC and ∠ACB are on opposite sides of AC')
c = r(c, 'אלו <strong>זוויות מתחלפות</strong> שוות ביחס לחוצה AC.', 'These are equal <strong>alternate angles</strong> relative to transversal AC.')
c = r(c, 'לכן:', 'Therefore:')
c = r(c, '>לתרגיל 4<', '>To Exercise 4<')

# Exercise 4
c = r(c, '<!-- ==================== תרגיל 4 ==================== -->', '<!-- ==================== Exercise 4 ==================== -->')
c = r(c, '<!-- ==================== תרגיל 4 ====================', '<!-- ==================== Exercise 4 ====================')
c = r(c, 'תרגיל 4 - מצא את זוגות הישרים המקבילים', 'Exercise 4 - Find the Parallel Line Pairs')
c = r(c, '<!-- ישר a -->', '<!-- Line a -->')
c = r(c, '<!-- ישר b -->', '<!-- Line b -->')
c = r(c, '<!-- ישר d -->', '<!-- Line d -->')
c = r(c, '<!-- ישר c -->', '<!-- Line c -->')
c = r(c, '<!-- ישר e -->', '<!-- Line e -->')
c = r(c, '<!-- ישר f -->', '<!-- Line f -->')
c = r(c, '<!-- קווים חותכים -->', '<!-- Transversal lines -->')
c = r(c, '<!-- תוויות זוויות -->', '<!-- Angle labels -->')
c = r(c, 'זוויות כמסומן בשרטוט', 'Angles as marked in the diagram')
c = r(c, 'מצא זוגות ישרים מקבילים ונמק:', 'Find pairs of parallel lines and justify:')
c = r(c, 'רמז: חפש זוויות מתאימות שוות', 'Hint: Look for equal corresponding angles')
c = r(c, 'כי שתיהן יוצרות זווית 110°', 'because both form a 110° angle')
c = r(c, '>עוד זוג<', '>Another pair<')

# Exercise 4 continued
c = r(c, '<!-- ==================== תרגיל 4 המשך ====================', '<!-- ==================== Exercise 4 continued ====================')
c = r(c, 'תרגיל 4 - עוד זוג מקביל', 'Exercise 4 - Another Parallel Pair')
c = r(c, '<!-- a מודגש -->', '<!-- a highlighted -->')
c = r(c, '<!-- d מודגש -->', '<!-- d highlighted -->')
c = r(c, '<!-- c מודגש -->', '<!-- c highlighted -->')
c = r(c, '<!-- f מודגש -->', '<!-- f highlighted -->')
c = r(c, '<div><strong>מצאנו:</strong> c || d (זוויות 110°)</div>', '<div><strong>Found:</strong> c || d (110° angles)</div>')
c = r(c, 'מצא עוד זוג מקביל:', 'Find another parallel pair:')
c = r(c, 'רמז: חפש זוויות 70° שוות', 'Hint: Look for equal 70° angles')
c = r(c, 'כי שתיהן יוצרות זווית 70°', 'because both form a 70° angle')
c = r(c, '<strong>סיכום:</strong>', '<strong>Summary:</strong>')
c = r(c, '>סיום<', '>Finish<')

# Final page
c = r(c, '<!-- ==================== סיום ====================', '<!-- ==================== Finish ====================')
c = r(c, 'Completed את כל התרגילים!', 'You completed all exercises!')
c = r(c, 'תשובות:', 'Answers:')
c = r(c, 'תרגיל 1:', 'Exercise 1:')
c = r(c, 'תרגיל 2:', 'Exercise 2:')
c = r(c, 'תרגיל 3:', 'Exercise 3:')
c = r(c, 'תרגיל 4:', 'Exercise 4:')
c = r(c, 'להתחיל מחדש', 'Start Over')

write_file('page2.html', c)
print('page2.html pass2 done')

# ============================================================
# page3.html - lots remaining
# ============================================================
c = read_file('page3.html')

# Progress
c = r(c, 'תרגיל <span id="currentEx">1</span> מתוך 14', 'Exercise <span id="currentEx">1</span> of 14')
c = r(c, 'בחר תרגיל', 'Choose Exercise')

# Exercise types
c = r(c, 'משוואה עם שברים', 'Equation with Fractions')
c = r(c, 'משוואה עם סוגריים', 'Equation with Brackets')
c = r(c, 'משוואה עם מכנה משתנה', 'Equation with Variable Denominator')
c = r(c, 'אי-שוויון', 'Inequality')

# Step titles
c = r(c, 'מציאת מכנה משותף', 'Finding the Common Denominator')
c = r(c, 'הכפלה במכנה המשותף', 'Multiplying by Common Denominator')
c = r(c, 'אחרי הכפלה ב-10', 'After Multiplying by 10')
c = r(c, 'פתרון המשוואה', 'Solving the Equation')
c = r(c, '>פתרון<', '>Solution<')
c = r(c, 'הכפלה במכנה ופתרון', 'Multiplying by Denominator and Solving')
c = r(c, 'מכפלת לכסונים', 'Cross Multiplication')
c = r(c, 'פירוק וצמצום', 'Factoring and Simplifying')
c = r(c, 'Collecting terms ופתרון', 'Collecting Terms and Solving')
c = r(c, 'Expand brackets ופישוט', 'Expanding Brackets and Simplifying')

# Questions
c = r(c, 'מהו המכנה המשותף?', 'What is the common denominator?')
c = r(c, 'המכנים הם:', 'The denominators are:')
c = r(c, 'נכפיל את <strong>כל האגפים</strong> ב-21 כדי להיפטר מהשברים',
    'We multiply <strong>both sides</strong> by 21 to eliminate the fractions')
c = r(c, 'מה מקבלים אחרי פתיחת כל הסוגריים?', 'What do we get after expanding all brackets?')
c = r(c, 'מה מקבלים אחרי Expand brackets ופישוט?', 'What do we get after expanding brackets and simplifying?')
c = r(c, 'מה נשאר אחרי חיסור \\(x^2\\) משני האגפים?', 'What remains after subtracting \\(x^2\\) from both sides?')
c = r(c, 'מה נשאר אחרי חיסור \\(x^2\\)?', 'What remains after subtracting \\(x^2\\)?')
c = r(c, 'מה המסקנה?', 'What is the conclusion?')

# Feedback
c = r(c, '21 הוא המכנה המשותף הקטן ביותר!', '21 is the least common denominator!')
c = r(c, 'אגף שמאל: 3x+6. אגף ימין: x+8+7x-28+21x = 29x-20', 'Left side: 3x+6. Right side: x+8+7x-28+21x = 29x-20')
c = r(c, '26 = 26x, לכן x = 1', '26 = 26x, therefore x = 1')
c = r(c, '10 מתחלק ב-2, ב-5 וב-10', '10 is divisible by 2, 5, and 10')
c = r(c, '5x+5+x-1 = 6x+4, ו-2x+6+10 = 2x+16', '5x+5+x-1 = 6x+4, and 2x+6+10 = 2x+16')
c = r(c, '4x = 12, לכן x = 3', '4x = 12, therefore x = 3')
c = r(c, '\\(x^2 + 3x - x^2 = x^2 - x^2\\) נותן \\(3x = 0\\)', '\\(x^2 + 3x - x^2 = x^2 - x^2\\) gives \\(3x = 0\\)')
c = r(c, 'אם 3x = 0, אז x = 0', 'If 3x = 0, then x = 0')
c = r(c, '\\(2 + x^2 - x^2 = x^2 + x - x^2\\) נותן \\(2 = x\\)', '\\(2 + x^2 - x^2 = x^2 + x - x^2\\) gives \\(2 = x\\)')
c = r(c, '5 = 5x, לכן x = 1', '5 = 5x, therefore x = 1')
c = r(c, '4x - 3x = 5, לכן x = 5', '4x - 3x = 5, therefore x = 5')
c = r(c, '\\(-3x = -8\\), לכן \\(x = \\frac{8}{3}\\)', '\\(-3x = -8\\), therefore \\(x = \\frac{8}{3}\\)')
c = r(c, '\\(11x = -2\\), לכן \\(x = -\\frac{2}{11}\\)', '\\(11x = -2\\), therefore \\(x = -\\frac{2}{11}\\)')
c = r(c, '4 = 4 נכון תמיד! זו זהות.', '4 = 4 is always true! This is an identity.')
c = r(c, '-18 = 0 הוא משפט שקרי!', '-18 = 0 is a false statement!')
c = r(c, '\\(16x < -4\\) נותן \\(x < -\\frac{1}{4}\\)', '\\(16x < -4\\) gives \\(x < -\\frac{1}{4}\\)')
c = r(c, '\\(-5x \\geq -30\\) הופך ל-\\(x \\leq 6\\) (הפכנו סימן!)', '\\(-5x \\geq -30\\) becomes \\(x \\leq 6\\) (sign flipped!)')
c = r(c, '\\(-3x < 12\\) הופך ל-\\(x > -4\\) (הפכנו סימן!)', '\\(-3x < 12\\) becomes \\(x > -4\\) (sign flipped!)')
c = r(c, '\\(-11x < 22\\) הופך ל-\\(x > -2\\) (הפכנו סימן!)', '\\(-11x < 22\\) becomes \\(x > -2\\) (sign flipped!)')

# Domain/substitution
c = r(c, '<strong>תחום הצבה:</strong> \\(x \\neq 2\\) (המכנה לא יכול להיות 0)', '<strong>Domain:</strong> \\(x \\neq 2\\) (denominator cannot be 0)')
c = r(c, '<strong>תחום הצבה:</strong> \\(x \\neq 2\\) וגם \\(x \\neq 0\\)', '<strong>Domain:</strong> \\(x \\neq 2\\) and \\(x \\neq 0\\)')
c = r(c, '<strong>תחום הצבה:</strong> \\(x \\neq -4\\)', '<strong>Domain:</strong> \\(x \\neq -4\\)')
c = r(c, '<strong>תחום הצבה:</strong> \\(x \\neq 0\\) וגם \\(x \\neq 3\\)', '<strong>Domain:</strong> \\(x \\neq 0\\) and \\(x \\neq 3\\)')

# Cross multiplication hint
c = r(c, 'כשיש \\(\\frac{a}{b} = \\frac{c}{d}\\), נכפיל לכסונים: \\(a \\cdot d = b \\cdot c\\)',
    'When we have \\(\\frac{a}{b} = \\frac{c}{d}\\), cross multiply: \\(a \\cdot d = b \\cdot c\\)')

# Factor hint
c = r(c, 'שימו לב! אפשר להוציא גורם משותף מהמונה: \\(4x + 16 = 4(x+4)\\)',
    'Note! We can factor out a common factor from the numerator: \\(4x + 16 = 4(x+4)\\)')

# Multiply note
c = r(c, 'נכפיל ב-\\((x-2)\\):', 'Multiply by \\((x-2)\\):')

# Answer options
c = r(c, 'אינסוף פתרונות (כל \\(x \\neq -4\\))', 'Infinite solutions (all \\(x \\neq -4\\))')
c = r(c, 'אין פתרון</button>', 'No solution</button>')
c = r(c, 'אין פתרון (משפט שקרי)', 'No solution (false statement)')
c = r(c, 'אינסוף פתרונות', 'Infinite solutions')
c = r(c, '>אין פתרון<', '>No solution<')

# Final titles
c = r(c, '>מצוין!<', '>Excellent!<')
c = r(c, '>נכון מאוד!<', '>Exactly right!<')
c = r(c, '>יופי!<', '>Great!<')
c = r(c, '>נהדר!<', '>Wonderful!<')
c = r(c, '>מדהים!<', '>Amazing!<')
c = r(c, '>נכון!<', '>Correct!<')
c = r(c, '>סיימת הכל!<', '>All done!<')

# Number line descriptions
c = r(c, 'עיגול פתוח (לא כולל), חץ שמאלה', 'Open circle (not included), arrow left')
c = r(c, 'עיגול סגור (כולל), חץ שמאלה', 'Closed circle (included), arrow left')
c = r(c, 'עיגול פתוח (לא כולל), חץ ימינה', 'Open circle (not included), arrow right')

# Domain check notes
c = r(c, '\\(\\frac{8}{3} \\neq 2\\) - בתחום ✓', '\\(\\frac{8}{3} \\neq 2\\) - in domain ✓')
c = r(c, 'בתחום ✓', 'In domain ✓')
c = r(c, 'אינסוף פתרונות - זו זהות!', 'Infinite solutions - this is an identity!')
c = r(c, '\\(\\emptyset\\) - הקבוצה הריקה', '\\(\\emptyset\\) - the empty set')

# Inequality hints
c = r(c, 'מחלקים ב-16 (מספר <strong>חיובי</strong>) - הסימן <strong>נשאר</strong>!',
    'Dividing by 16 (a <strong>positive</strong> number) - the sign <strong>stays</strong>!')
c = r(c, '<strong>שימו לב!</strong> מחלקים ב-(-5) - מספר <strong>שלילי</strong> - הופכים את הסימן!',
    '<strong>Note!</strong> Dividing by (-5) - a <strong>negative</strong> number - flip the sign!')
c = r(c, '<strong>שימו לב!</strong> מחלקים ב-(-3) - מספר <strong>שלילי</strong> - הופכים את הסימן!',
    '<strong>Note!</strong> Dividing by (-3) - a <strong>negative</strong> number - flip the sign!')
c = r(c, '<strong>שימו לב!</strong> מחלקים ב-(-11) - מספר <strong>שלילי</strong> - הופכים את הסימן!',
    '<strong>Note!</strong> Dividing by (-11) - a <strong>negative</strong> number - flip the sign!')

# Nav buttons
c = r(c, '>הקודם<', '>Prev<')
c = r(c, '>הבא<', '>Next<')
c = r(c, '>חזור להתחלה<', '>Back to Start<')

# Menu items JS
c = r(c, '`<div class="menu-item-num">תרגיל ${titles[i][0]}</div>', '`<div class="menu-item-num">Ex. ${titles[i][0]}</div>')

# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

write_file('page3.html', c)
print('page3.html pass2 done')

# ============================================================
# page5.html - remaining
# ============================================================
c = read_file('page5.html')

# Read remaining Hebrew
# Let's look for specific patterns
c = r(c, 'lang="he"', 'lang="en"')  # in case missed
c = r(c, 'dir="rtl"', 'dir="ltr"')  # in case missed

# All Hebrew text in page5
c = r(c, '>פונקציות - משאית מחיפה<', '>Functions - Truck from Haifa<')
c = r(c, 'משאית נוסעת מחיפה לכיוון דרום.', 'A truck travels from Haifa heading south.')
c = r(c, 'הגרף שלהלן מציג את המרחק של המשאית מחיפה (בק"מ) כפונקציה של הזמן (בשעות).',
    "The graph below shows the truck's distance from Haifa (in km) as a function of time (in hours).")
c = r(c, 'גרף מרחק-זמן', 'Distance-Time Graph')
c = r(c, 'מרחק מחיפה (ק"מ)', 'Distance from Haifa (km)')
c = r(c, 'זמן (שעות)', 'Time (hours)')
c = r(c, '>שאלות<', '>Questions<')

# Questions (generic patterns)
c = r(c, 'א.', 'A.')
c = r(c, 'ב.', 'B.')
c = r(c, 'ג.', 'C.')
c = r(c, 'ד.', 'D.')
c = r(c, 'ה.', 'E.')

# More specific Q&A patterns
c = r(c, 'מה המרחק של המשאית מחיפה לאחר שעתיים?', 'What is the distance of the truck from Haifa after 2 hours?')
c = r(c, 'באיזו שעה הגיעה המשאית למרחק 120 ק"מ מחיפה?', 'At what time did the truck reach 120 km from Haifa?')
c = r(c, 'מה קרה בין השעה 2 ל-3?', 'What happened between hour 2 and 3?')
c = r(c, 'המשאית עצרה', 'The truck stopped')
c = r(c, 'המשאית נסעה', 'The truck drove')
c = r(c, 'המשאית חזרה', 'The truck returned')
c = r(c, 'מה המהירות הממוצעת', 'What is the average speed')
c = r(c, 'של המשאית ב-2 השעות הראשונות?', 'of the truck in the first 2 hours?')
c = r(c, 'מהי המהירות', 'What is the speed')
c = r(c, 'בין השעות', 'between hours')

# Answers
c = r(c, '120 ק"מ', '120 km')
c = r(c, '160 ק"מ', '160 km')
c = r(c, '200 ק"מ', '200 km')
c = r(c, '80 ק"מ', '80 km')
c = r(c, '60 ק"מ', '60 km')
c = r(c, '300 ק"מ', '300 km')
c = r(c, '100 קמ"ש', '100 km/h')
c = r(c, '120 קמ"ש', '120 km/h')
c = r(c, '80 קמ"ש', '80 km/h')
c = r(c, '60 קמ"ש', '60 km/h')
c = r(c, '40 קמ"ש', '40 km/h')

# Feedback
c = r(c, 'לאחר שעתיים', 'After 2 hours')
c = r(c, 'הגרף מראה', 'The graph shows')
c = r(c, 'קטע אופקי = עצירה', 'Horizontal segment = stop')
c = r(c, 'מהירות = מרחק / זמן', 'Speed = distance / time')

# Button/score
c = r(c, 'כל הכבוד! ענית נכון על כל השאלות!', 'Well done! You answered all questions correctly!')
c = r(c, 'התחלה מחדש', 'Start Over')
c = r(c, 'התחל מחדש', 'Start Over')

# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

write_file('page5.html', c)
print('page5.html pass2 done')

# ============================================================
# page5_q6a_table.html
# ============================================================
c = read_file('page5_q6a_table.html')

# More specific patterns
c = r(c, 'השלימו את הטבלה', 'Complete the table')
c = r(c, 'הכניסו את הערכים', 'Enter the values')
c = r(c, 'בדקו', 'Check')
c = r(c, 'תשובה נכונה', 'Correct answer')
c = r(c, 'תשובה שגויה', 'Wrong answer')
c = r(c, 'כל הכבוד', 'Well done')
c = r(c, 'חנות פלאפל', 'Falafel shop')
c = r(c, 'מנות', 'portions')
c = r(c, 'רווח', 'Profit')
c = r(c, 'שקלים', 'shekels')
c = r(c, 'הפסד', 'Loss')
c = r(c, 'נקודת איזון', 'Break-even point')
c = r(c, 'מספר מנות', 'Number of portions')

# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

write_file('page5_q6a_table.html', c)
print('page5_q6a_table.html pass2 done')

# ============================================================
# page5_q6bcdef_analysis.html
# ============================================================
c = read_file('page5_q6bcdef_analysis.html')

# More specific patterns
c = r(c, 'שיפוע', 'Slope')
c = r(c, 'ערך', 'Value')
c = r(c, 'משמעות', 'Meaning')
c = r(c, 'הרווח', 'The profit')
c = r(c, 'ההפסד', 'The loss')
c = r(c, 'החנות', 'The shop')
c = r(c, 'מתחילה להרוויח', 'starts making a profit')
c = r(c, 'מנות', 'portions')
c = r(c, 'שקלים', 'shekels')
c = r(c, 'הוצאות קבועות', 'Fixed expenses')
c = r(c, 'כל הכבוד', 'Well done')

# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

write_file('page5_q6bcdef_analysis.html', c)
print('page5_q6bcdef_analysis.html pass2 done')

# ============================================================
# page6.html
# ============================================================
c = read_file('page6.html')

# Need to see what's still Hebrew
# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

write_file('page6.html', c)
print('page6.html pass2 done')

print('\n=== PASS 2 DONE ===')
