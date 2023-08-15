document.addEventListener("DOMContentLoaded", function () {
    var analyseButton = document.getElementById('analyse_button');
    var formDiv = document.getElementById('analyse_form_div');
    var detailsDiv = document.getElementById('analyse_details');
    var analysed = false;

    analyseButton.addEventListener('click', function () {
        

        // Collect and format input data
        var jobTitle = document.getElementById('jobTitle').value;
        var requirements = document.getElementById('requirements').value;
        var skills = document.getElementById('skills').value;
        var aboutCompany = document.getElementById('aboutCompany').value;
        var Responsibilities = document.getElementById('responsibilities').value;

        var inputData = [
            "TITLE : " + jobTitle,
            "REQUIREMENTS : " + requirements,
            "SKILLS : " + skills,
            "ABOUT COMPANY : " + aboutCompany,
            "RESPONSIBILITY : " + Responsibilities
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
            document.getElementById('response_box').style.display = 'block'
            document.getElementById('analyse_score').textContent = 'Overall Score: ' + data["Overall Score"];
            document.getElementById('overall_review').textContent = 'Overall Review: ' + data["Overall Review"];

            var prosList = document.getElementById('pros');
            data.Pros.forEach(function (item, index) {
                var listItem = document.createElement('li');
                listItem.textContent = (index + 1) + '. ' + item;
                prosList.appendChild(listItem);
            });

            var consList = document.getElementById('cons');
            data.Cons.forEach(function (item, index) {
                var listItem = document.createElement('li');
                listItem.textContent = (index + 1) + '. ' + item;
                consList.appendChild(listItem);
            });

            var suggestionsList = document.getElementById('suggestions');
            data.Suggestions.forEach(function (item, index) {
                var listItem = document.createElement('li');
                listItem.textContent = (index + 1) + '. ' + item;
                suggestionsList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
    });
});

