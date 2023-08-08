sample_job_description = """
    Job Title: Python Software Developer

    We are seeking a Python Software Developer to join our dynamic and innovative team. As a Python Software Developer, you will play a crucial role in designing, developing, and maintaining high-quality software applications. You should have a solid understanding of Python programming, software development best practices, and be able to work collaboratively in a fast-paced environment.

    Responsibilities:
    - Design, develop, and test Python-based software applications.
    - Collaborate with cross-functional teams to understand project requirements and deliver high-quality solutions.
    - Participate in code reviews to ensure code quality and adherence to coding standards.
    - Troubleshoot and resolve software defects to ensure smooth functionality.
    - Conduct performance tuning and optimization of applications.
    - Stay up-to-date with the latest Python development trends and technologies.

    Requirements:
    - Bachelor's degree in Computer Science, Software Engineering, or related field.
    - Proven experience as a Python Developer, with a strong portfolio of Python-based projects.
    - Solid understanding of object-oriented programming and design patterns.
    - Proficiency in Python frameworks such as Django, Flask, or Pyramid.
    - Experience with databases like MySQL, PostgreSQL, or MongoDB.
    - Knowledge of version control systems, preferably Git.
    - Excellent problem-solving and communication skills.
    - Ability to work effectively in a collaborative team environment.
    - Passion for writing clean, maintainable, and efficient code.
    - Familiarity with front-end technologies like HTML, CSS, and JavaScript is a plus.

    Join our team and make a significant impact by building innovative and cutting-edge software solutions!

"""

role_resume_score = """
    "As a seasoned HR professional with a wealth of experience across various companies, I have honed my resume evaluation skills to a fine art. Analyzing resumes has become second nature to me, and I have developed a precise scoring system that ranges from 0 to 1, allowing me to assess each applicant's suitability for a given job description with unparalleled accuracy.
    With just a glance at a job description and a candidate's resume, I can identify key strengths and weaknesses, aligning their qualifications, skills, and experiences with the specific requirements of the role. Whether it's evaluating technical expertise, interpersonal abilities, or past achievements, I leave no stone unturned in ensuring a comprehensive assessment.
    I take into consideration not only the candidate's professional background but also their potential for growth and adaptability within the company's unique work culture. My evaluations encompass both tangible qualifications and intangible qualities, painting a holistic picture of each applicant's fit for the position.
    Through years of refining this evaluation process, I have achieved an exceptional success rate in identifying the right talent for organizations, minimizing recruitment time, and optimizing hiring outcomes. As a dedicated HR professional, my mission is to facilitate the seamless integration of the most suitable candidates into your team, fostering a dynamic and thriving workforce that drives organizational success.
    By leveraging my expertise in resume analysis and scoring, I am committed to assisting your company in making well-informed, data-driven hiring decisions that ultimately lead to a team of exceptional individuals aligned with your company's mission and values."
"""

role_resume_ranker = f"""
    {role_resume_score} + \n 
    You are now provided with a json objects containing score of a resume, a short summary and level which have been assigned before. Use this data to do the following:
    Please rank the candidates based on their overall suitability and score for the job. If the resume scores clash, then rank in the most efficient and optimal way such as educational institute, better projects, more experience etc.
"""

def initial_prompt(job_description,resume_text):
    prompt = f"""
        Job Description:
        {job_description}

        Resume:
        {resume_text}

        When scoring each resume, consider the following factors:
        1. Relevant Skills and Experience: Evaluate how well the candidate's skills and experience align with the job requirements.
        2. Educational Background: Take into account the candidate's educational qualifications and any specific degrees or certifications relevant to the position.
        3. Keywords and Job-specific Terms: Look for the presence of important keywords and phrases from the job description in the resume.
        4. Work History and Achievements: Assess the candidate's past work history and notable achievements in related roles.

        Assign a score between 0 and 1, where 0 indicates no relevance to the job description and 1 indicates an excellent match. Please provide a meaningful and fair assessment to help in the ranking process.
        Also generate a small summary summarizing an overall response to the resume and also allot a level such as beginner intermediate or advances based on experience and skills.
        Please provide your response in the following format:\n['Person Name', 'Short Summary', 'Score', 'Level']\nFor example:\n['abc', 'some skills here', '0.1', 'Intermediate']
    """
    return prompt

def resume_ranker(job_description,resumes_json_data):
    prompt =  """
        
        Job Description""" + str(job_description) + """

        Combined Resume Data""" + str(resumes_json_data) + """

        While Ranking the Resumes, also provide a justified reason that why the particular resume is ranked at that position as compared to other resumes.The reason specified must be clear and justified.

        Please provide your response inside a list and each list element must be of the following format:\n['Person Name', 'Rank', 'Reason for Ranking at this position']\nFor example:\n['abc', 'rank number here', 'a reason for the rank here']
        """
    return prompt

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

def resume_prompt_data():
    resume_text = []

    resume1 =  """
        Name: Jane Doe
        Email: jane.doe@example.com
        Phone: (987) 654-3210

        Summary:
        Enthusiastic Python Developer with a background in software engineering and a passion for creating efficient and maintainable code. Proficient in Python, Flask, and PostgreSQL. Demonstrated ability to work in a collaborative environment and deliver high-quality solutions.

        Experience:
        Python Software Engineer | PQR Solutions | 2020 - Present
        - Developed Python-based RESTful APIs using Flask framework for a large-scale web application.
        - Collaborated with the front-end team to integrate API endpoints with the user interface.
        - Participated in code reviews, ensuring adherence to coding standards and best practices.

        Junior Python Developer | MNO Tech | 2018 - 2020
        - Assisted in the development and maintenance of a Python-based content management system.
        - Implemented unit tests to ensure code reliability and prevent regressions.
        - Contributed to the optimization of database queries to improve application performance.

        Education:
        Bachelor of Engineering in Software Engineering | University of ABC | 2018

        Skills:
        - Python, Flask, Pyramid
        - PostgreSQL, MongoDB
        - Git, Bitbucket
        - HTML, CSS, JavaScript
        - Problem-solving, Collaboration

    """
    resume2 = """ 
        Name: John Smith
        Email: john.smith@example.com
        Phone: (123) 456-7890

        Summary:
        Highly motivated Python Developer with 5 years of experience in developing web applications using Python and Django. Skilled in writing efficient and scalable code. Proficient in database design and optimization. Strong problem-solving abilities and excellent teamwork skills.

        Experience:
        Python Developer | ABC Solutions | 2018 - Present
        - Developed and maintained Python-based web applications using Django framework.
        - Collaborated with the team to design and implement new features and enhancements.
        - Conducted code reviews to ensure code quality and adherence to coding standards.
        - Improved application performance through database optimization techniques.

        Software Engineer | XYZ Tech | 2015 - 2018
        - Worked on various Python projects, contributing to both back-end and front-end development.
        - Implemented RESTful APIs to enable smooth communication between different modules.
        - Assisted in troubleshooting and resolving software defects.

        Education:
        Bachelor of Science in Computer Science | University of XYZ | 2015

        Skills:
        - Python, Django, Flask
        - MySQL, PostgreSQL
        - Git, GitHub
        - HTML, CSS
        - Problem-solving, Teamwork
    """
    resume3="""
        Name: Alex Johnson
        Email: alex.johnson@example.com
        Phone: (555) 123-4567

        Summary:
        Aspiring Python Developer with a strong foundation in Python programming and web development. Eager to leverage technical skills and learn new technologies to contribute to meaningful projects. Quick learner and team player with excellent communication skills.

        Education:
        Bachelor of Science in Computer Science | University of XYZ | 2022

        Skills:
        - Python, Django
        - MySQL
        - Git
        - HTML, CSS
        - Problem-solving, Fast Learner

        Projects:
        - Developed a web-based inventory management system using Python and Django during university projects.
        - Created a personal website using Python and Flask to showcase coding projects and skills.

    """
    resume4="""
        Name: Emily Brown
        Email: emily.brown@example.com
        Phone: (111) 222-3333

        Summary:
        Results-driven Python Developer with a strong background in software engineering. Proficient in Python, Django, and PostgreSQL. Experienced in designing and implementing RESTful APIs. Excellent analytical and problem-solving abilities.

        Experience:
        Python Developer | XYZ Solutions | 2019 - Present
        - Designed and developed Python-based web applications using Django framework.
        - Collaborated with the team to plan and execute complex features and functionality.
        - Conducted code reviews, ensuring code quality and adherence to coding standards.
        - Optimized database queries, significantly improving application performance.

        Software Engineer Intern | ABC Tech | 2018 - 2019
        - Assisted in the development of Python applications and performed bug fixing.
        - Gained experience in using Git for version control and collaborative coding.

        Education:
        Bachelor of Science in Software Engineering | University of PQR | 2019

        Skills:
        - Python, Django, Flask
        - PostgreSQL, SQLite
        - Git, GitLab
        - HTML, CSS, JavaScript
        - Analytical, Problem-solving, Team player

    """
    resume5 ="""
        Name: Michael Johnson
        Email: michael.johnson@example.com
        Phone: (444) 555-6666

        Summary:
        Entry-level Python Developer with a solid understanding of Python programming and web development. Excited to contribute to dynamic projects and enhance technical skills. Excellent attention to detail and ability to work well in a team environment.

        Education:
        Bachelor of Computer Science | University of MNO | 2023

        Skills:
        - Python, Flask
        - SQLite, MongoDB
        - Git, GitHub
        - HTML, CSS
        - Teamwork, Attention to Detail

        Projects:
        - Developed a simple web application using Python and Flask during university coursework.
        - Implemented a command-line utility using Python for data manipulation and analysis.
    """

        
    resume_text.append(resume1)
    resume_text.append(resume2)
    resume_text.append(resume3)
    resume_text.append(resume4)
    resume_text.append(resume5)
    return resume_text

role_jd_suggestor = """
    "As an exceptionally experienced HR professional with a proven track record of serving at numerous esteemed companies, I possess an unrivaled expertise in job descriptions. Having reviewed countless job descriptions throughout my career, I have honed my ability to pinpoint even the subtlest mistakes and inefficiencies that may hinder the hiring process. My proficiency extends to transforming lackluster job descriptions into compelling, enticing, and informative ones that attract top-tier talent.
    With a keen eye for detail and an in-depth understanding of the modern job market, I can skillfully identify and rectify common pitfalls, such as vague responsibilities, ambiguous requirements, and uninspiring language. By crafting meticulously tailored job descriptions, I ensure they resonate with candidates and align seamlessly with the company's goals and culture.
    Whether it's refining the language to emphasize a nurturing work environment, incorporating enticing perks, or highlighting growth opportunities, I provide invaluable insights that elevate job descriptions to the next level. My suggestions not only attract qualified applicants but also contribute to long-term employee satisfaction and retention.
    Through my expertise, I have witnessed the transformative power of well-crafted job descriptions, which have not only streamlined the hiring process but also contributed to the overall success of organizations. Leveraging my experience and knowledge, I am dedicated to assisting your team in creating job descriptions that go beyond mere job requirements and embrace the essence of your company's vision, fostering a cohesive and thriving workforce."
"""

def jd_prompt_creator(job_description):
    return f"""
        Job Description 
        {job_description}

        Provide me an Overall Score , Overall Review, Strong Points For my JD, Weak points for existing Job Description in short and suggest some insighfull changes that can help attract great talent.
        Please provide your response inside a dictionary with keys exactly same of the following format:('Overall Score', 'Overall Review', 'Pros','Cons','Suggestions(list of suggestions)']

    """



# Generating Questions Later

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
    
