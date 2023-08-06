def initial_prompt(job_description,resume_text):
    return f"""
        As an HR manager at [Company Name], you are responsible for evaluating resumes for the position of [Job Title]. Please assess the following resume's suitability for the job based on the provided job description:

        Job Description:
        {job_description}

        Resume:
        {resume_text}

        When scoring each resume, consider the following factors:
        1. Relevant Skills and Experience: Evaluate how well the candidate's skills and experience align with the job requirements.
        2. Educational Background: Take into account the candidate's educational qualifications and any specific degrees or certifications relevant to the position.
        3. Keywords and Job-specific Terms: Look for the presence of important keywords and phrases from the job description in the resume.
        4. Work History and Achievements: Assess the candidate's past work history and notable achievements in related roles.

        Assign a score between 0 and 100, where 0 indicates no relevance to the job description and 100 indicates an excellent match. Please provide a meaningful and fair assessment to help in the ranking process.
        Also generate a small summary summarizing an overall response to the resume and also allot a level such as beginner intermediate or advances based on experience and skills.
        Return the response in a json format as following {'Person Name','Short Summary','Score','Level'}

    """

def resume_ranker(job_description,resumes_json_data):
    return f"""
        You are an HR manager evaluating candidates for a job at [Company Name]. Below is the job description:

        {job_description}

        Please rank the candidates based on their overall suitability for the job. If the resume scores clash, then rank in the most efficient and optimal way .

        {resumes_json_data}

        Return the output in JSON format with the following fields:
        - Rank
        - Person Name
        - Score
        - Short Summary
        - Reason for Rank

    """

def question_generator(job_description,resume_text):
    return f"""
        You are an HR manager conducting a mock test for evaluating candidates applying for a job at [Company Name]. The test will assess their knowledge and skills in line with the job description and their resume information. Below is the job description:

        {job_description}

        Please use the provided resume data for each candidate to create 10 multiple-choice questions (MCQs) based on the specified fields in their resume. Each question should be designed to challenge the test taker's understanding and expertise in relevant technologies and experiences. Aim for a moderate difficulty level where the questions are not too easy but a bit challenging.

        Additionally, if the job is related to coding, please include one moderate coding question that tests the candidate's practical coding abilities.

        Each MCQ should have four options (A, B, C, D), with only one correct answer.

        {resume_text}

        Add a point in this to return the output in JSON format with the following fields:
        - JSON Questions
        - JSON Options
        - JSON Answer
"""
    
