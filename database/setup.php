<?php
$db = new SQLite3('database/pyqs.db');

if (!$db) {
    die("Connection failed: " . $db->lastErrorMsg());
}

$query = "
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course TEXT NOT NULL,
    subject TEXT NOT NULL,
    year INTEGER,
    question_text TEXT NOT NULL,
    options TEXT,
    correct_answer TEXT,
    explanation TEXT
);";

if ($db->exec($query)) {
    echo "Table 'questions' created successfully or already exists.\n";
} else {
    echo "Error creating table: " . $db->lastErrorMsg() . "\n";
}

$questions = [
    [
        'course' => 'NEET',
        'subject' => 'Physics',
        'year' => 2023,
        'question_text' => 'A ball is thrown vertically upward. What is its velocity at the highest point?',
        'options' => '["9.8 m/s", "0 m/s", "-9.8 m/s", "Depends on the mass"]',
        'correct_answer' => '0 m/s',
        'explanation' => 'At the highest point, the ball momentarily stops before changing direction, so its velocity is 0 m/s.'
    ],
    [
        'course' => 'NEET',
        'subject' => 'Chemistry',
        'year' => 2023,
        'question_text' => 'What is the chemical formula for water?',
        'options' => '["H2O2", "CO2", "H2O", "CH4"]',
        'correct_answer' => 'H2O',
        'explanation' => 'Water is composed of two hydrogen atoms and one oxygen atom.'
    ],
    [
        'course' => 'JEE',
        'subject' => 'Maths',
        'year' => 2023,
        'question_text' => 'What is the derivative of x^2?',
        'options' => '["2x", "x", "x/2", "x^2"]',
        'correct_answer' => '2x',
        'explanation' => 'Using the power rule, the derivative of x^n is nx^(n-1).'
    ]
];

// Check if data already exists to avoid duplicates
$count = $db->querySingle("SELECT COUNT(*) as count FROM questions");
if ($count == 0) {
    $stmt = $db->prepare('INSERT INTO questions (course, subject, year, question_text, options, correct_answer, explanation) VALUES (:course, :subject, :year, :question_text, :options, :correct_answer, :explanation)');

    foreach ($questions as $q) {
        $stmt->bindValue(':course', $q['course'], SQLITE3_TEXT);
        $stmt->bindValue(':subject', $q['subject'], SQLITE3_TEXT);
        $stmt->bindValue(':year', $q['year'], SQLITE3_INTEGER);
        $stmt->bindValue(':question_text', $q['question_text'], SQLITE3_TEXT);
        $stmt->bindValue(':options', $q['options'], SQLITE3_TEXT);
        $stmt->bindValue(':correct_answer', $q['correct_answer'], SQLITE3_TEXT);
        $stmt->bindValue(':explanation', $q['explanation'], SQLITE3_TEXT);

        if ($stmt->execute()) {
            echo "Record inserted successfully.\n";
        } else {
            echo "Error inserting record: " . $db->lastErrorMsg() . "\n";
        }
    }
} else {
    echo "Data already exists, skipping insertion.\n";
}

$db->close();
?>