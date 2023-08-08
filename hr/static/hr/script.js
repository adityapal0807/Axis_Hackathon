document.addEventListener("DOMContentLoaded", function () {
    var analyseButton = document.getElementById('analyse_button');
    var formDiv = document.getElementById('analyse_form_div');
    var detailsDiv = document.getElementById('analyse_details');
    var analysed = false;

    analyseButton.addEventListener('click', function () {
        if (!analysed) {
            // Move form to the right side
            formDiv.style.flex = '0 0 50%';

            // Show the details on the left side
            detailsDiv.style.display = 'block';

            // Disable the Analyse button
            analyseButton.disabled = true;

            analysed = true;

            // Collect and format input data
            var jobTitle = document.getElementById('jobTitle').value;
            var requirements = document.getElementById('requirements').value;
            var skills = document.getElementById('skills').value;
            var aboutCompany = document.getElementById('aboutCompany').value;
            var eligibility = document.getElementById('eligibility').value;

            var inputData = [
                "TITLE : " + jobTitle,
                "REQUIREMENTS : " + requirements,
                "SKILLS : " + skills,
                "ABOUT COMPANY : " + aboutCompany,
                "ELIGIBILITY : " + eligibility
            ];

            var job_description = inputData.join('\n');
            console.log(job_description);

            fetch('/api/analyse_jd', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    job_description: job_description
                })
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response data here
                console.log('API Response:', data);
                document.getElementById('analyse_score').textContent = 'Overall Score: ' + data["Overall Score"];
                document.getElementById('overall_review').textContent = 'Overall Review: ' + data["Overall Review"];

                var pros = data.Pros.map(function (item, index) {
                    return (index + 1) + '. ' + item;
                });
                document.getElementById('pros').textContent = 'Pros:\n' + pros.join('\n');

                var cons = data.Cons.map(function (item, index) {
                    return (index + 1) + '. ' + item;
                });
                document.getElementById('cons').textContent = 'Cons:\n' + cons.join('\n');

                var suggestions = data.Suggestions.map(function (item, index) {
                    return (index + 1) + '. ' + item;
                });
                document.getElementById('suggestions').textContent = 'Suggestions:\n' + suggestions.join('\n');
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});