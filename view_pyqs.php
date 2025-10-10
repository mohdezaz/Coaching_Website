<?php
// Database connection
$db = new SQLite3('database/pyqs.db');

// Get course and subject from URL
$course = isset($_GET['course']) ? $_GET['course'] : '';
$subject = isset($_GET['subject']) ? $_GET['subject'] : '';

// Fetch questions from the database
$stmt = $db->prepare('SELECT * FROM questions WHERE course = :course AND subject = :subject ORDER BY year DESC');
$stmt->bindValue(':course', $course, SQLITE3_TEXT);
$stmt->bindValue(':subject', $subject, SQLITE3_TEXT);
$results = $stmt->execute();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo htmlspecialchars($course . ' ' . $subject); ?> PYQs - Cluster Classes</title>
    <link rel="stylesheet" href="css/style.css?v=2">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <?php include 'templates/header.php'; ?>

    <main class="container">
        <section class="pyq-section">
            <h2><?php echo htmlspecialchars($course . ' ' . $subject); ?> Previous Year Questions</h2>
            <div class="pyq-list">
                <?php while ($row = $results->fetchArray(SQLITE3_ASSOC)): ?>
                    <div class="pyq-item">
                        <div class="pyq-question-container">
                            <p class="pyq-question"><strong>Q:</strong> <?php echo htmlspecialchars($row['question_text']); ?> <span class="pyq-year">(<?php echo htmlspecialchars($row['year']); ?>)</span></p>
                            <div class="pyq-options">
                                <?php
                                $options = json_decode($row['options']);
                                foreach ($options as $option): ?>
                                    <div class="pyq-option"><?php echo htmlspecialchars($option); ?></div>
                                <?php endforeach; ?>
                            </div>
                        </div>
                        <div class="pyq-answer-container">
                            <button class="toggle-answer-btn">Show Answer</button>
                            <div class="pyq-answer" style="display: none;">
                                <p><strong>Correct Answer:</strong> <?php echo htmlspecialchars($row['correct_answer']); ?></p>
                                <p><strong>Explanation:</strong> <?php echo htmlspecialchars($row['explanation']); ?></p>
                            </div>
                        </div>
                    </div>
                <?php endwhile; ?>
            </div>
        </section>
    </main>

    <?php include 'templates/footer.php'; ?>

    <script src="js/main.js"></script>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const answerButtons = document.querySelectorAll('.toggle-answer-btn');
        answerButtons.forEach(button => {
            button.addEventListener('click', () => {
                const answerDiv = button.nextElementSibling;
                if (answerDiv.style.display === 'none') {
                    answerDiv.style.display = 'block';
                    button.textContent = 'Hide Answer';
                } else {
                    answerDiv.style.display = 'none';
                    button.textContent = 'Show Answer';
                }
            });
        });
    });
    </script>
</body>
</html>