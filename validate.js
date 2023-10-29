// Add an event listener to the form's submit event
document.querySelector('form').addEventListener('submit', function(event) {
    var questions = document.querySelectorAll('.question');
    var allAnswered = true;

    for (var i = 0; i < questions.length; i++) {
        var options = questions[i].querySelectorAll('input[type="radio"]');
        var isAnswered = false;

        for (var j = 0; j < options.length; j++) {
            if (options[j].checked) {
                isAnswered = true;
                break;
            }
        }

        if (!isAnswered) {
            allAnswered = false;
            break;
        }
    }

    // If not all questions are answered, prevent the form submission
    if (!allAnswered) {
        event.preventDefault();
        alert('Please answer all questions before submitting.');
    }
});
