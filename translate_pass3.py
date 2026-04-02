#!/usr/bin/env python3
"""Third pass - catch ALL remaining Hebrew."""
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

HEB = re.compile(r'[\u0590-\u05FF]')

def check(name, content):
    lines = content.split('\n')
    remaining = []
    for i, line in enumerate(lines, 1):
        if HEB.search(line):
            remaining.append(f"  Line {i}: {line.strip()[:120]}")
    if remaining:
        print(f"WARNING: {name} still has {len(remaining)} lines with Hebrew:")
        for l in remaining[:10]:
            print(l)
        if len(remaining) > 10:
            print(f"  ... and {len(remaining)-10} more")
    else:
        print(f"OK: {name} - no Hebrew remaining")

# ============================================================
# page2.html
# ============================================================
c = read_file('page2.html')
c = r(c, 'רמז: חפש Corresponding angles שוות', 'Hint: Look for equal corresponding angles')
c = r(c, 'א. 105° | ב. 55° | ג. 65°', 'A. 105° | B. 55° | C. 65°')
c = r(c, 'א. 25° | ב. 60° | ג. 110° | ד. 70°', 'A. 25° | B. 60° | C. 110° | D. 70°')
check('page2.html', c)
write_file('page2.html', c)

# ============================================================
# page3.html
# ============================================================
c = read_file('page3.html')

# Exercise numbers with Hebrew letters
c = r(c, "<!-- ========== Exercise 1: 30א ========== -->", "<!-- ========== Exercise 1: 30a ========== -->")
c = r(c, ">30א<", ">30a<")
c = r(c, "<!-- ========== Exercise 2: 30ב ========== -->", "<!-- ========== Exercise 2: 30b ========== -->")
c = r(c, ">30ב<", ">30b<")
c = r(c, "מה מקבלים אחרי Expanding Brackets and Simplifying?", "What do we get after expanding brackets and simplifying?")
c = r(c, ">א<", ">a<")
c = r(c, ">ב<", ">b<")
c = r(c, ">ג<", ">c<")
c = r(c, ">ד<", ">d<")
c = r(c, ">מעולה!</", ">Excellent!</")
c = r(c, ">מעולה!<", ">Excellent!<")
c = r(c, "Infinite solutions - זו זהות!", "Infinite solutions - this is an identity!")

# JS array with Hebrew
c = r(c, "['30א',", "['30a',")
c = r(c, "['30ב',", "['30b',")
c = r(c, "['א', 'x(x+3)", "['a', 'x(x+3)")
c = r(c, "['ב', '2 + x²", "['b', '2 + x²")
c = r(c, "['ג', 'x(x-3)", "['c', 'x(x-3)")
c = r(c, "['ד', 'x(x+4)", "['d', 'x(x+4)")
c = r(c, "['א', 'x/(x-2)", "['a', 'x/(x-2)")
c = r(c, "['ב', '6/(x-2)", "['b', '6/(x-2)")
c = r(c, "['ג', '(4x+16)", "['c', '(4x+16)")
c = r(c, "['ד', '6/x", "['d', '6/x")

check('page3.html', c)
write_file('page3.html', c)

# ============================================================
# page4_q5_pricing.html
# ============================================================
c = read_file('page4_q5_pricing.html')

c = r(c, 'שאלה 5 - גרפים של מחירים', 'Question 5 - Price Graphs')
c = r(c, 'השוואת הצעות מחיר: אורן מול תומר', 'Comparing Price Proposals: Oren vs. Tomer')
c = r(c, 'התקדמות: <span id="progressCount">0</span> מתוך 5 שאלות', 'Progress: <span id="progressCount">0</span> of 5 questions')
c = r(c, 'מחיר (₪)', 'Price (NIS)')
c = r(c, 'שטח (מ"ר)', 'Area (sq. m)')
c = r(c, '>גרף I<', '>Graph I<')
c = r(c, '>גרף II<', '>Graph II<')
c = r(c, 'נקודת חיתוך', 'Intersection point')
c = r(c, '<div style="margin-bottom: 10px;"><strong>נתון:</strong></div>', '<div style="margin-bottom: 10px;"><strong>Given:</strong></div>')
c = r(c, '(x = שטח במ"ר, Price = מחיר ב-₪)', '(x = area in sq. m, y = price in NIS)')
c = r(c, '>א<', '>A<')
c = r(c, 'איזה גרף שייך לכל אחד מהרצפים?', 'Which graph belongs to each gardener?')
c = r(c, 'גרף I שייך ל:', 'Graph I belongs to:')
c = r(c, '>תומר<', '>Tomer<')
c = r(c, '>אורן<', '>Oren<')
c = r(c, 'Correct! גרף I עובר דרך הראשית', 'Correct! Graph I passes through the origin')
c = r(c, 'גרף II שייך ל:', 'Graph II belongs to:')
c = r(c, 'Correct! גרף II מתחיל ב-700', 'Correct! Graph II starts at 700')
c = r(c, '>ב1<', '>B1<')
c = r(c, 'עבור איזה שטח המחיר זהה אצל שניהם?', 'For what area is the price the same for both?')
c = r(c, 'מ"ר', 'sq. m')
c = r(c, '>בדוק<', '>Check<')
c = r(c, 'Correct! בדיוק בנקודת החיתוך', 'Correct! Exactly at the intersection point')
c = r(c, '>ב2<', '>B2<')
c = r(c, 'מה המחיר עבור אותו שטח?', 'What is the price for that area?')
c = r(c, 'מצוין! 48×25 = 1200 ₪', 'Excellent! 48×25 = 1200 NIS')
c = r(c, '>ג1<', '>C1<')
c = r(c, 'עבור שטח של 17 מ"ר - מי זול יותר?', 'For an area of 17 sq. m - who is cheaper?')
c = r(c, '>ג2<', '>C2<')
c = r(c, 'בכמה הוא זול יותר?', 'By how much is he cheaper?')
c = r(c, 'מעולה! 1040 - 816 = 224 ₪', 'Excellent! 1040 - 816 = 224 NIS')
c = r(c, 'כל הכבוד! סיימת את כל השאלות!', 'Well done! You completed all the questions!')
c = r(c, 'למדת לזהות גרפים לפי נוסחאות ולחשב נקודות חיתוך!', 'You learned to identify graphs by formulas and calculate intersection points!')

# JS hints
c = r(c, "'רמז: שימו לב איפה כל גרף חותך את ציר Y (כשx=0)'", "'Hint: Notice where each graph intersects the Y axis (when x=0)'")
c = r(c, "'רמז: Tomer: 48×0 = 0, Oren: 700+20×0 = 700'", "'Hint: Tomer: 48×0 = 0, Oren: 700+20×0 = 700'")
c = r(c, "'רמז: גרף שעובר דרך הראשית (0,0) מתחיל מ-0...'", "'Hint: A graph passing through the origin (0,0) starts from 0...'")
c = r(c, "'רמז: בדקו את נקודת ההתחלה של כל גרף על ציר Y'", "'Hint: Check the starting point of each graph on the Y axis'")
c = r(c, "'רמז: איזו נוסחה נותנת 700 כשx=0?'", "'Hint: Which formula gives 700 when x=0?'")
c = r(c, "'רמז: 700 + 20×0 = 700 - זה הגרף שמתחיל ב-700'", "'Hint: 700 + 20×0 = 700 - this is the graph starting at 700'")
c = r(c, "'רמז: חפשו את נקודת החיתוך של שני הגרפים'", "'Hint: Find the intersection point of the two graphs'")
c = r(c, "'רמז: פתרו: 48x = 700 + 20x'", "'Hint: Solve: 48x = 700 + 20x'")
c = r(c, "'רמז: 28x = 700, אז x = ?'", "'Hint: 28x = 700, so x = ?'")
c = r(c, "'רמז: הציבו את השטח שמצאתם בנוסחה של תומר'", "'Hint: Substitute the area you found in Tomer\\'s formula'")
c = r(c, "'רמז: חשבו 48 × (התשובה מב1)'", "'Hint: Calculate 48 × (the answer from B1)'")
c = r(c, "'רמז: 48 × 25 = ?'", "'Hint: 48 × 25 = ?'")
c = r(c, "'רמז: חשבו את המחיר אצל כל אחד עבור 17 מ\"ר'", "'Hint: Calculate the price for each gardener for 17 sq. m'")
c = r(c, "'רמז: Tomer: 48×17 = ?, Oren: 700+20×17 = ?'", "'Hint: Tomer: 48×17 = ?, Oren: 700+20×17 = ?'")
c = r(c, "'רמז: השוו: 816 מול 1040 - מי נותן פחות?'", "'Hint: Compare: 816 vs 1040 - who charges less?'")
c = r(c, "'רמז: חסרו את המחיר הזול מהמחיר היקר'", "'Hint: Subtract the cheaper price from the more expensive one'")
c = r(c, "'רמז: אורן - תומר = ההפרש'", "'Hint: Oren - Tomer = the difference'")
c = r(c, "'רמז: 1040 - 816 = ?'", "'Hint: 1040 - 816 = ?'")
c = r(c, "'ניסיון ' + attempts[id] + ' - נסה שוב!'", "'Attempt ' + attempts[id] + ' - try again!'")

# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

check('page4_q5_pricing.html', c)
write_file('page4_q5_pricing.html', c)

# ============================================================
# page5.html - full re-read and fix
# ============================================================
c = read_file('page5.html')

c = r(c, 'משאית יצאה מחיפE.', 'A truck left Haifa.')
c = r(c, 'במהלך הנסיעה עצרה פעמיים.', 'During the trip it stopped twice.')
c = r(c, 'הגרף שלפניכם מתאר את המרחק מחיפה בהתאם לזמן שעבר מתחילת הנסיעE.', 'The graph below describes the distance from Haifa as a function of time elapsed since the start of the trip.')
c = r(c, 'גרף המרחק מחיפה כפונקציה של הזמן', 'Distance from Haifa as a Function of Time')
c = r(c, 'מסלול המשאית', 'Truck route')
c = r(c, 'הדגשה', 'Highlight')

# Question A
c = r(c, '<!-- שאלה א - השלמת הטבלה -->', '<!-- Question A - Completing the table -->')
c = r(c, 'A. השלימו את הטבלה על סמך הגרף הנתון.', 'A. Complete the table based on the given graph.')
c = r(c, '>משלכם<', '>your value<')

# Question B
c = r(c, '<!-- שאלה ב - פרקי זמן שהמשאית לא נסעה -->', '<!-- Question B - Time periods when the truck was not moving -->')
c = r(c, 'B. באילו פרקי זמן לא נסעה המשאית? הסבירו.', 'B. During which time periods was the truck not moving? Explain.')
c = r(c, 'שעות 1-2 ו-4-5 (כי הגרף עולה לאט)', 'Hours 1-2 and 4-5 (because the graph rises slowly)')
c = r(c, 'שעות 2-3 ו-5-6 (כי הגרף אופקי - המרחק לא משתנה)', 'Hours 2-3 and 5-6 (because the graph is horizontal - distance does not change)')
c = r(c, 'שעות 6-7 (כי הגרף יורד)', 'Hours 6-7 (because the graph descends)')
c = r(c, 'שעות 0-1 ו-3-4 (כי המשאית האטה)', 'Hours 0-1 and 3-4 (because the truck slowed down)')

# Question C
c = r(c, '<!-- שאלה ג - האם חזרה לחיפה -->', '<!-- Question C - Did the truck return to Haifa -->')
c = r(c, 'C. האם חזרה המשאית לחיפה? הסבירו.', 'C. Did the truck return to Haifa? Explain.')
c = r(c, 'כן, כי הגרף יורד בסוף', 'Yes, because the graph descends at the end')
c = r(c, 'לא, כי בסוף (x=7) המרחק הוא 100 km ולא 0', 'No, because at the end (x=7) the distance is 100 km not 0')
c = r(c, 'כן, כי היא עצרה פעמיים', 'Yes, because it stopped twice')
c = r(c, 'לא ניתן לדעת מהגרף', 'Cannot be determined from the graph')

# Question D
c = r(c, '<!-- שאלה ד - מרחק מרבי -->', '<!-- Question D - Maximum distance -->')
c = r(c, 'D. מה היה המרחק המרבי שלה מחיפה במהלך הנסיעה?', 'D. What was its maximum distance from Haifa during the trip?')

# Question E
c = r(c, '<!-- שאלה ה - שני מרחקים שונים באותו זמן -->', '<!-- Question E - Two different distances at the same time -->')
c = r(c, 'E. האם ייתכן שבנקודת זמן מסוימת במהלך הנסיעה הייתה המשאית בשני מרחקים שונים מחיפה?', 'E. Is it possible that at a certain point in time during the trip the truck was at two different distances from Haifa?')
c = r(c, 'לא, כי בכל רגע נתון המשאית יכולה להיות רק במקום אחד', 'No, because at any given moment the truck can only be in one place')
c = r(c, 'כן, כשהיא עצרה', 'Yes, when it stopped')
c = r(c, 'כן, כשהיא חזרה לכיוון חיפה', 'Yes, when it returned toward Haifa')
c = r(c, 'תלוי במהירות הנסיעה', 'Depends on the travel speed')

# Question F
c = r(c, '<!-- שאלה ו - האם לכל x מתאים y יחיד -->', '<!-- Question F - Does each x have a unique y -->')
c = r(c, 'ו. האם לפי הגרף הנתון לכל ערך של המשתנה זמן (x) מתאים ערך יחיד של המשתנה מרחק מחיפה (y)? הסבירו.', 'F. According to the given graph, does each value of the time variable (x) correspond to a unique value of the distance from Haifa variable (y)? Explain.')
c = r(c, 'כן, לכל ערך x יש ערך y יחיד - זו הגדרת פונקציה', 'Yes, each x value has a unique y value - this is the definition of a function')
c = r(c, 'לא, כי לפעמים הגרף אופקי', 'No, because sometimes the graph is horizontal')
c = r(c, 'לא, כי הגרף גם עולה וגם יורד', 'No, because the graph both rises and falls')
c = r(c, 'רק בחלק מהזמנים', 'Only at some times')

# Score
c = r(c, 'ענית על <span id="correctCount">0</span> מתוך <span id="totalCount">6</span> שאלות נכון', 'You answered <span id="correctCount">0</span> out of <span id="totalCount">6</span> questions correctly')

# Definition box
c = r(c, '<h3>הגדרה: מהי פונקציה?</h3>', '<h3>Definition: What is a Function?</h3>')
c = r(c, 'התאמה שבה <strong>לכל ערך של משתנה מסוים מתאים ערך אחד ויחיד</strong> של משתנה אחר נקראת <strong>פונקציה</strong>.', 'A correspondence in which <strong>each value of a certain variable corresponds to one and only one</strong> value of another variable is called a <strong>function</strong>.')
c = r(c, 'לדוגמה, במשימה זו לכל ערך של זמן (x) מתאים ערך יחיד של מרחק (y).', 'For example, in this task, each time value (x) corresponds to a unique distance value (y).')
c = r(c, 'כמו כן, שימו לב שניתן להציג את הפונקציה בצורה מילולית, בטבלה ובדרך גרפית.', 'Also note that a function can be represented verbally, in a table, and graphically.')

# JS feedbacks
c = r(c, "correct: \"Correct! מהגרף: בזמן x=1 המרחק 50 ק\\\"מ, בזמן x=3.5 המרחק 150 ק\\\"מ, בזמן x=7 המרחק 100 ק\\\"מ.\"", 'correct: "Correct! From the graph: at time x=1 the distance is 50 km, at time x=3.5 the distance is 150 km, at time x=7 the distance is 100 km."')
c = r(c, "incorrect: \"Incorrect. קראו בזהירות מהגרף: x=1 נמצא על הקו מ-(0,0) ל-(2,100) ולכן y=50. x=3.5 נמצא על הקו מ-(3,100) ל-(5,200) ולכן y=150. x=7 הוא סוף הגרף ולכן y=100.\"", 'incorrect: "Incorrect. Read carefully from the graph: x=1 is on the line from (0,0) to (2,100) so y=50. x=3.5 is on the line from (3,100) to (5,200) so y=150. x=7 is the end of the graph so y=100."')
c = r(c, "correct: \"Correct! הגרף אופקי בשעות 2-3 ו-5-6. כאשר הגרף אופקי, המרחק לא משתנה - כלומר המשאית לא נעE.\",", 'correct: "Correct! The graph is horizontal at hours 2-3 and 5-6. When the graph is horizontal, the distance does not change - meaning the truck is not moving.",')
c = r(c, "incorrect: \"Incorrect. עצירה = קטע אופקי בגרף (המרחק לא משתנה). הקטעים האופקיים הם בשעות 2-3 ו-5-6.\"", 'incorrect: "Incorrect. A stop = horizontal segment in graph (distance does not change). The horizontal segments are at hours 2-3 and 5-6."')
c = r(c, "correct: \"Correct! בסוף הנסיעה (x=7) המרחק מחיפה הוא 100 ק\\\"מ. כדי לחזור לחיפה, הגרף צריך להגיע ל-y=0.\",", 'correct: "Correct! At the end of the trip (x=7) the distance from Haifa is 100 km. To return to Haifa, the graph would need to reach y=0.",')
c = r(c, "incorrect: \"Incorrect. חזרה לחיפה = הגרף מגיע ל-y=0. בסוף הגרף (x=7) הערך הוא y=100, כלומר המשאית נשארה במרחק 100 ק\\\"מ מחיפE.\"", 'incorrect: "Incorrect. Returning to Haifa = graph reaches y=0. At the end of the graph (x=7) the value is y=100, meaning the truck stayed 100 km from Haifa."')
c = r(c, "correct: \"Correct! הנקודה הגבוהה ביותר בגרף היא y=200 ק\\\"מ, והיא מושגת בין שעות 5-6.\",", 'correct: "Correct! The highest point on the graph is y=200 km, reached between hours 5-6.",')
c = r(c, "incorrect: \"Incorrect. המרחק המרבי הוא הנקודה הגבוהה ביותר בגרף. הפסגה היא ב-y=200 ק\\\"מ.\"", 'incorrect: "Incorrect. The maximum distance is the highest point on the graph. The peak is at y=200 km."')
c = r(c, "correct: \"Correct! בכל רגע נתון המשאית יכולה להיות רק במקום אחD. לכן לכל ערך של זמן יש ערך יחיד של מרחק.\",", 'correct: "Correct! At any given moment the truck can only be in one place. Therefore each time value has a unique distance value.",')
c = r(c, "incorrect: \"Incorrect. פיזית, משאית לא יכולה להיות בשני מקומות בו-זמנית. לכל רגע (x) יש מיקום יחיד (y).\"", 'incorrect: "Incorrect. Physically, a truck cannot be in two places simultaneously. Each moment (x) has a unique location (y)."')
c = r(c, "correct: \"Correct! לכל ערך של x מתאים ערך y יחיד - וזו בדיוק ההגדרה של פונקציE. הגרף עובר את \\\"מבחן הקו האנכי\\\".\",", 'correct: "Correct! Each x value corresponds to a unique y value - and that is exactly the definition of a function. The graph passes the vertical line test.",')
c = r(c, "incorrect: \"Incorrect. הקשר הוא פונקציה כי לכל זמן (x) מתאים מרחק יחיד (y). קטעים אופקיים או ירידות לא משנים את העובדה שלכל x יש y יחיD.\"", 'incorrect: "Incorrect. The relation is a function because each time (x) corresponds to a unique distance (y). Horizontal segments or descents do not change the fact that each x has a unique y."')

check('page5.html', c)
write_file('page5.html', c)

# ============================================================
# page5_q6a_table.html
# ============================================================
c = read_file('page5_q6a_table.html')

c = r(c, 'שאלה 6 - מרחק מחיפה - מילוי טבלה', 'Question 6 - Distance from Haifa - Fill Table')
c = r(c, 'שאלה 6 - קריאת גרף: מרחק מחיפה', 'Question 6 - Reading a Graph: Distance from Haifa')
c = r(c, '<strong>משאית יצאה מחיפה. במהלך הנסיעה עצרה פעמיים.</strong>', '<strong>A truck left Haifa. During the trip it stopped twice.</strong>')
c = r(c, 'הגרף שלפניכם מתאר את המרחק מחיפה בהתאם לזמן שעבר מתחילת הנסיעה.', 'The graph below describes the distance from Haifa as a function of time elapsed since the start of the trip.')
c = r(c, 'מרחק מחיפה (ק"מ)', 'Distance from Haifa (km)')
c = r(c, 'זמן (שעות)', 'Time (hours)')
c = r(c, 'א. Complete the table על סמך הגרף', 'A. Complete the table based on the graph')
c = r(c, 'מצאו את המרחק מחיפה (y) עבור כל ערך של זמן (x) בגרף:', 'Find the distance from Haifa (y) for each time value (x) in the graph:')
c = r(c, 'זמן (שעות)', 'Time (hours)')
c = r(c, 'מרחק מחיפה<br>(ק"מ)', 'Distance from Haifa<br>(km)')
c = r(c, '>בדוק<', '>Check<')
c = r(c, 'התקדמות:', 'Progress:')
c = r(c, 'Well done! מילאת את כל הטבלה Correct!', 'Well done! You filled in the entire table correctly!')
c = r(c, 'הצלחת לקרוא את כל הערכים מהגרף בצורה מושלמת!', 'You successfully read all the values from the graph perfectly!')

# JS hints
c = r(c, "'מצא את x=1 על ציר הזמן'", "'Find x=1 on the time axis'")
c = r(c, "'עלה ישר למעלה עד הגרף'", "'Go straight up to the graph'")
c = r(c, "'קרא את ערך y בציר המרחק'", "'Read the y value on the distance axis'")
c = r(c, "'מצא את x=3 על ציר הזמן'", "'Find x=3 on the time axis'")
c = r(c, "'זו נקודה על הגרף - עלה למעלה'", "'This is a point on the graph - go up'")
c = r(c, "'הגרף מגיע לשיא כאן'", "'The graph reaches its peak here'")
c = r(c, "'מצא את x=3.5 (בין 3 ל-4)'", "'Find x=3.5 (between 3 and 4)'")
c = r(c, "'שים לב - הגרף שטוח כאן!'", "'Note - the graph is flat here!'")
c = r(c, "'המשאית עצרה - המרחק לא משתנה'", "'The truck stopped - distance does not change'")
c = r(c, "'מצא את x=4 על ציר הזמן'", "'Find x=4 on the time axis'")
c = r(c, "'הגרף יורד כאן - המשאית חוזרת'", "'The graph descends here - the truck is returning'")
c = r(c, "'קרא את ערך y'", "'Read the y value'")
c = r(c, "'מצא את x=7 על ציר הזמן'", "'Find x=7 on the time axis'")
c = r(c, "'זו נקודת הסיום של הנסיעה'", "'This is the end point of the trip'")
c = r(c, "'המשאית חזרה לחיפה!'", "'The truck returned to Haifa!'")
c = r(c, "התשובה:", "The answer:")

# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

check('page5_q6a_table.html', c)
write_file('page5_q6a_table.html', c)

# ============================================================
# page5_q6bcdef_analysis.html
# ============================================================
c = read_file('page5_q6bcdef_analysis.html')

c = r(c, 'שאלה 6 - ניתוח מרחק מחיפה', 'Question 6 - Distance from Haifa Analysis')
c = r(c, 'שאלה 6 - משאית מחיפה', 'Question 6 - Truck from Haifa')
c = r(c, 'ניתוח גרף מרחק-זמן', 'Distance-Time Graph Analysis')
c = r(c, '<strong>משאית יצאה מחיפה. במהלך הנסיעה עצרה פעמיים.</strong>', '<strong>A truck left Haifa. During the trip it stopped twice.</strong>')
c = r(c, 'הגרף שלפניכם מתאר את המרחק מחיפה בהתאם לזמן שעבר מתחילת הנסיעה.', 'The graph below describes the distance from Haifa as a function of time elapsed since the start of the trip.')
c = r(c, '<h3>הגרף</h3>', '<h3>The Graph</h3>')
c = r(c, 'alt="גרף מרחק מחיפה"', 'alt="Distance from Haifa graph"')
c = r(c, '<h3>הטבלה</h3>', '<h3>The Table</h3>')
c = r(c, 'alt="טבלת ערכים"', 'alt="Value table"')

# Questions
c = r(c, '<!-- שאלה ב -->', '<!-- Question B -->')
c = r(c, 'ב. באילו פרקי זמן לא נסעה המשאית? הסבירו.', 'B. During which time periods was the truck not moving? Explain.')
c = r(c, 'בחרו את התשובה הנכונה:', 'Choose the correct answer:')
c = r(c, 'בין שעה 0 ל-1 ובין שעה 4 ל-5', 'Between hour 0 and 1, and between hour 4 and 5')
c = r(c, 'בין שעה 1 ל-2 ובין שעה 3 ל-3.5 (כי הגרף אופקי - המרחק לא משתנה)', 'Between hour 1 and 2, and between hour 3 and 3.5 (because the graph is horizontal - distance does not change)')
c = r(c, 'בין שעה 5 ל-7 (כי הגרף יורד)', 'Between hour 5 and 7 (because the graph descends)')
c = r(c, 'המשאית נסעה כל הזמן ללא הפסקה', 'The truck traveled continuously without stopping')
c = r(c, '>בדוק תשובה<', '>Check Answer<')

c = r(c, '<!-- שאלה ג -->', '<!-- Question C -->')
c = r(c, 'ג. האם חזרה המשאית לחיפה? הסבירו.', 'C. Did the truck return to Haifa? Explain.')
c = r(c, 'כן, המשאית חזרה לחיפה כי בזמן x=7 המרחק הוא y=0', 'Yes, the truck returned to Haifa because at time x=7 the distance is y=0')
c = r(c, 'לא, המשאית לא חזרה כי בסוף היא נשארה במרחק 100 ק"מ', 'No, the truck did not return because at the end it remained 100 km away')
c = r(c, 'לא ניתן לדעת מהגרף', 'Cannot be determined from the graph')
c = r(c, 'כן, כי היא עצרה פעמיים בדרך', 'Yes, because it stopped twice on the way')

c = r(c, '<!-- שאלה ד -->', '<!-- Question D -->')
c = r(c, 'ד. מה היה המרחק המרבי שלה מחיפה במהלך הנסיעה?', 'D. What was the maximum distance from Haifa during the trip?')
c = r(c, '100 ק"מ', '100 km')
c = r(c, '150 ק"מ', '150 km')
c = r(c, '200 ק"מ', '200 km')
c = r(c, '250 ק"מ', '250 km')

c = r(c, '<!-- שאלה ה -->', '<!-- Question E -->')
c = r(c, 'ה. האם ייתכן שבשני זמנים שונים היה אותו מרחק מחיפה?', 'E. Is it possible that at two different times the distance from Haifa was the same?')
c = r(c, 'כן, כי בדרך הלוך ובדרך חזור עברה המשאית באותם מרחקים', 'Yes, because on the way out and the way back the truck passed through the same distances')
c = r(c, 'לא, לכל זמן יש מרחק שונה', 'No, each time has a different distance')
c = r(c, 'לא, כי זו פונקציה', 'No, because it is a function')
c = r(c, 'רק בזמן העצירות', 'Only during stops')

c = r(c, '<!-- שאלה ו -->', '<!-- Question F -->')
c = r(c, 'ו. האם y (המרחק) הוא פונקציה חד-חד-ערכית של x (הזמן)?', 'F. Is y (the distance) a one-to-one function of x (the time)?')
c = r(c, 'כן, כי לכל זמן מתאים מרחק יחיד', 'Yes, because each time corresponds to a unique distance')
c = r(c, 'לא, כי יש מרחקים שמתאימים ליותר מזמן אחד (למשל 150 ק"מ בהלוך ובחזור)', 'No, because some distances correspond to more than one time (e.g. 150 km on the way out and back)')
c = r(c, 'כן, כי הגרף עולה ויורד', 'Yes, because the graph rises and falls')
c = r(c, 'לא ניתן לקבוע', 'Cannot be determined')

c = r(c, '<strong>תזכורת:</strong> פונקציה <span class="highlight">חד-חד-ערכית</span> היא פונקציה שבה לכל Value y מתאים לכל היותר Value x אחד.', '<strong>Reminder:</strong> A <span class="highlight">one-to-one</span> function is a function where each y value corresponds to at most one x value.')
c = r(c, 'במילים אחרות: כל קו אופקי חותך את הגרף לכל היותר בנקודה אחת.', 'In other words: every horizontal line intersects the graph at most at one point.')

c = r(c, 'סיימת את כל השאלות!', 'You completed all questions!')

# JS comments
c = r(c, 'בין שעה 1-2 ו-3-3.5 (גרף אופקי)', 'Between hour 1-2 and 3-3.5 (horizontal graph)')
c = r(c, 'כן, חזרה לחיפה (y=0 ב-x=7)', 'Yes, returned to Haifa (y=0 at x=7)')
c = r(c, '200 ק"מ', '200 km')
c = r(c, 'כן, בהלוך ובחזור', 'Yes, on the way out and back')
c = r(c, 'לא, לא חד-חד-ערכית', 'No, not one-to-one')

# JS feedback strings
c = r(c, "correct: '✓ Correct! כאשר הגרף אופקי, המרחק מחיפה לא משתנה - כלומר המשאית עומדת במקום. זה קורה בין שעה 1 ל-2 ובין שעה 3 ל-3.5.',",
    "correct: '✓ Correct! When the graph is horizontal, the distance from Haifa does not change - meaning the truck is stationary. This occurs between hour 1 and 2, and between hour 3 and 3.5.',")
c = r(c, "wrong: '✗ Incorrect. חפשו את הקטעים שבהם הגרף אופקי (שטוח) - שם המשאית לא נעה כי המרחק לא משתנה.'",
    "wrong: '✗ Incorrect. Look for segments where the graph is horizontal (flat) - there the truck is not moving because the distance does not change.'")
c = r(c, "correct: '✓ Correct! בסוף הנסיעה (בזמן x=7) הגרף מגיע לנקודה y=0, כלומר המשאית חזרה לחיפה.',",
    "correct: '✓ Correct! At the end of the trip (at time x=7) the graph reaches y=0, meaning the truck returned to Haifa.',")
c = r(c, "wrong: '✗ Incorrect. בדקו את הגרף בנקודה x=7 - מה Value ה-y שם? האם הוא שווה ל-0?'",
    "wrong: '✗ Incorrect. Check the graph at point x=7 - what is the y value there? Is it equal to 0?'")
c = r(c, "correct: '✓ Correct! הנקודה הגבוהה ביותר בגרף היא 200 ק\"מ, וזה המרחק המרבי שהמשאית התרחקה מחיפה.',",
    "correct: '✓ Correct! The highest point on the graph is 200 km, which is the maximum distance the truck traveled from Haifa.',")
c = r(c, "wrong: '✗ Incorrect. המרחק המרבי הוא הנקודה הגבוהה ביותר בגרף (הפסגה).'",
    "wrong: '✗ Incorrect. The maximum distance is the highest point on the graph (the peak).'")
c = r(c, "correct: '✓ Correct! כשהמשאית נסעה מחיפה והתרחקה, ואז חזרה - היא עברה באותם מרחקים פעמיים (פעם בהלוך ופעם בחזור).',",
    "correct: '✓ Correct! When the truck traveled from Haifa and moved away, then returned - it passed through the same distances twice (once going and once returning).',")
c = r(c, "wrong: '✗ Incorrect. חשבו: כשהמשאית נוסעת הלוך וחזור, האם היא עוברת באותם מקומות יותר מפעם אחת?'",
    "wrong: '✗ Incorrect. Think: when the truck travels back and forth, does it pass through the same locations more than once?'")
c = r(c, "correct: '✓ Correct! הפונקציה אינה חד-חד-ערכית כי יש ערכי מרחק (y) שמתאימים ליותר מזמן אחד (x). למשל, קו אופקי ב-y=150 חותך את הגרף בשתי נקודות.',",
    "correct: '✓ Correct! The function is not one-to-one because there are distance values (y) that correspond to more than one time (x). For example, a horizontal line at y=150 intersects the graph at two points.',")
c = r(c, "wrong: '✗ Incorrect. בפונקציה חד-חד-ערכית, לכל Value y מתאים לכל היותר Value x אחד. האם זה המצב כאן?'",
    "wrong: '✗ Incorrect. In a one-to-one function, each y value corresponds to at most one x value. Is that the case here?'")

c = r(c, "alert('אנא בחר תשובה');", "alert('Please select an answer');")

# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

check('page5_q6bcdef_analysis.html', c)
write_file('page5_q6bcdef_analysis.html', c)

# ============================================================
# page6.html
# ============================================================
c = read_file('page6.html')

c = r(c, 'Page 6 - שאלה מסכמת: הפונקציה הקווית', 'Page 6 - Summary Question: The Linear Function')
c = r(c, 'ניקוד', 'Score')
c = r(c, '>שאלה מסכמת: הפונקציה הקווית<', '>Summary Question: The Linear Function<')
c = r(c, 'Page 6 - חופשת חנוכה תשפ"ה', "Page 6 - Hanukkah Break 5785")

# Questions
c = r(c, '<!-- Question א -->', '<!-- Question A -->')
c = r(c, 'א. מצאו את הפונקציה f(x)', 'A. Find the function f(x)')
c = r(c, 'f(x) עוברת דרך ראשית הצירים O(0,0).', 'f(x) passes through the origin O(0,0).')
c = r(c, '<!-- Question ב -->', '<!-- Question B -->')
c = r(c, 'ב. מצאו את שיעור ה-x של הנקודה B', 'B. Find the x-coordinate of point B')
c = r(c, 'נתון ששיעור ה-y של הנקודה B הוא 6. B נמצאת על g(x).', 'Given that the y-coordinate of point B is 6. B is on g(x).')
c = r(c, '<!-- Question ג -->', '<!-- Question C -->')
c = r(c, 'ג. מצאו את הפונקציה g(x)', 'C. Find the function g(x)')
c = r(c, 'g(x) עוברת דרך D(0,12) ו-C(4,0).', 'g(x) passes through D(0,12) and C(4,0).')
c = r(c, '<!-- Question ד -->', '<!-- Question D -->')
c = r(c, 'ד. מצאו את שיעורי הנקודה E', 'D. Find the coordinates of point E')
c = r(c, 'E נמצאת על f(x).', 'E is on f(x).')
c = r(c, '<!-- Question ה - True/False -->', '<!-- Question E - True/False -->')
c = r(c, 'ה. טענות נכון/Incorrect', 'E. True/False Statements')
c = r(c, '1. אורך הקטע DE הוא 10 יח\'', '1. The length of segment DE is 10 units')
c = r(c, '>נכון<', '>True<')
c = r(c, '2. שטח המשולש △ABC הוא 30 יח"ר', '2. The area of triangle △ABC is 30 sq. units')
c = r(c, '<!-- Question ו -->', '<!-- Question F -->')
c = r(c, 'ו. משוואות הקטעים CE ו-AD', 'F. Equations of segments CE and AD')
c = r(c, '1. משוואת הקטע CE:', '1. Equation of segment CE:')
c = r(c, '2. משוואת הקטע AD:', '2. Equation of segment AD:')
c = r(c, '<!-- Question ז -->', '<!-- Question G -->')
c = r(c, 'ז. סדר שטחי המשולשים לפי גודלם', 'G. Order triangle areas by size')
c = r(c, 'סדרו את המשולשים ΔCEO, ΔBDE, ו-ΔADE מהקטן לגדול:', 'Order the triangles ΔCEO, ΔBDE, and ΔADE from smallest to largest:')
c = r(c, 'שטח CEO = 12 יח"ר | שטח BDE = 24 יח"ר | שטח ADE = 24 יח"ר', 'Area CEO = 12 sq. units | Area BDE = 24 sq. units | Area ADE = 24 sq. units')
c = r(c, '<!-- Question ח -->', '<!-- Question H -->')
c = r(c, 'ח. משוואות ישרים נוספים', 'H. Additional Line Equations')
c = r(c, '1. משוואת הישר העובר דרך B ומקביל לציר ה-x:', '1. Equation of the line through B parallel to the x-axis:')
c = r(c, '2. משוואת הישר העובר דרך C ומקביל לציר ה-y:', '2. Equation of the line through C parallel to the y-axis:')

# JS
c = r(c, "feedback.textContent = 'Correct! תשובה מצוינת!';", "feedback.textContent = 'Correct! Excellent answer!';")
c = r(c, "feedback.textContent = 'Incorrect. התשובה הנכונה: ' + correctAnswers[q];", "feedback.textContent = 'Incorrect. The correct answer is: ' + correctAnswers[q];")
c = r(c, "const correctText = tfAnswers[q] ? 'נכון' : 'Incorrect';", "const correctText = tfAnswers[q] ? 'True' : 'False';")
c = r(c, "feedback.textContent = 'Incorrect. התשובה הנכונה: ' + correctText;", "feedback.textContent = 'Incorrect. The correct answer is: ' + correctText;")
c = r(c, "feedback.textContent = 'Incorrect. התשובה הנכונה: ' + segAnswers[q];", "feedback.textContent = 'Incorrect. The correct answer is: ' + segAnswers[q];")
c = r(c, "feedback.textContent = 'Incorrect. התשובה הנכונה: ' + lineAnswers[q];", "feedback.textContent = 'Incorrect. The correct answer is: ' + lineAnswers[q];")

# Footer
c = r(c, '© פותח ע"י שיר סברוני', '\u00a9 Developed by Shir Sivroni')

check('page6.html', c)
write_file('page6.html', c)

print('\n=== PASS 3 DONE ===')
