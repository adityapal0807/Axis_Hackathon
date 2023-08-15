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
    Please rank the candidates based on their overall suitability and score for the job. If the resume scores clash, then rank in the most efficient and optimal way such as educational institute, better projects, more experience etc.Level parameter must be used.
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
        Please provide your response inside a dictionary with keys exactly same of the following format:("Person_Email_ID", "Score", "Short_Summary","level")
    """
    return prompt

def resume_ranker(job_description,resumes_json_data):
    prompt =  """
        
        Job Description \n""" + str(job_description) + """\n

        Combined Resume Data\n""" + str(resumes_json_data) + """\n

        While Ranking the Resumes, also provide a justified reason that why the particular resume is ranked at that position as compared to other resumes.The reason specified must be clear and justified.
        
        Please provide your response inside a list of dictionary with keys exactly same of the following format:("Person_Email_ID", "Rank", "Score" , "Reason(contains the reason for the given rank)", "Short_Summary","level") so that it helps extracting later using json.loads. Keys must be enclosed in doubleqoutes,not single.
        """
    return prompt

role_resume_ranker = f"""
    {role_resume_score} + \n 
    You are now provided with a json objects containing score of a resume, a short summary and level which have been assigned before. Use this data to do the following:
    Please rank the candidates based on their overall suitability and score for the job. If the resume scores clash, then rank in the most efficient and optimal way such as educational institute, better projects, more experience etc.Level parameter must be used.
"""

role_question_generator = """
    As an HR manager, your task is to create a comprehensive mock test that assesses the problem-solving skills of candidates applying for a position at [Company Name]. The test will focus on evaluating their expertise in the key skills outlined in the job description.
"""

def question_generator(job_description):
    return f"""
        Job Description:
        {job_description}

        Imagine you are developing software and need to assess candidates' proficiency in various essential skills commonly used in the field. Your goal is to create a set of multiple-choice questions (MCQs) that focus on specific skills required for software development. These questions should evaluate candidates' ability to apply their knowledge effectively to practical scenarios.

        For each skill, design a question that presents a real-world scenario or problem related to that skill. Create four options (A, B, C, D), with only one correct answer among them. The questions and options should be clear, concise, and aligned with the skill being assessed.

        Instructions:

        Choose specific skills relevant to software development, such as problem-solving, version control, database querying, algorithm complexity, code readability, debugging techniques, efficient code writing, unit testing, collaborative development, and code documentation.
        Craft each question to challenge candidates' understanding and application of the selected skill.
        Ensure that the questions clearly state the problem or scenario being presented.
        Create plausible options for each question that represent different approaches or answers related to the skill being assessed.
        Indicate the correct answer by labeling it accordingly (e.g., Option A, Option B).
        Add one or two coding related questions also.
        Remember, the aim is to create MCQs that accurately evaluate candidates' proficiency in specific skills within the software development domain. Focus on providing questions that reflect practical challenges and scenarios faced by software developers.
        Please provide your response inside a list of dictionary with keys exactly same of the following format:("question", "(list of options)", "correct(correct option list index)") so that it helps extracting later using json.loads. Keys must be enclosed in doubleqoutes,not single.
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
        Please provide your response inside a dictionary with keys exactly same of the following format:('Overall Score', 'Overall Review', 'Pros','Cons','Suggestions(list of suggestions)')

    """

role_situation = """
    I am an advanced AI-driven Situational Question Generator specializing in assisting HR teams and hiring managers in evaluating job candidates effectively. With my deep understanding of job roles, industry trends, and the nuances of effective communication, I create tailored situational questions that gauge a candidate's responses to relevant work scenarios, specifically designed to assess their problem-solving skills. My goal is to help you identify candidates who not only meet the job requirements but also possess the problem-solving and critical-thinking skills essential for success in your organization.

    Through careful analysis of the provided job description, I craft situational questions that accurately reflect the challenges and responsibilities associated with the role. Each question is designed to assess a candidate's ability to navigate real-world situations, handle problems, make informed decisions, and showcase their expertise. The scenarios I create are carefully balanced to maintain a moderate difficulty level, ensuring that candidates are challenged while remaining within the scope of the job requirements.

    By using my situational questions during interviews or assessments, you can gain valuable insights into how candidates approach and resolve job-related challenges. You'll be able to assess their thought processes, problem-solving capabilities, communication skills, adaptability, and alignment with your company's values and goals. I'm here to support your hiring process by providing a structured and consistent way to evaluate candidates, ultimately helping you build a high-performing and cohesive team.

    Partner with me to enhance your candidate evaluation process and identify top talent that not only meets the job description but also demonstrates the potential to excel and thrive within your organization.
"""

def create_situation(job_description):
    return f"""
        Job Description 
        {job_description}

        Given the job description provided, please generate a situational question that assesses a candidate's problem-handling skills and response to a relevant work scenario. The question should be moderate in difficulty and strictly aligned with the job requirements. Consider a situation where the candidate needs to demonstrate problem-solving skills, decision-making abilities, and an understanding of the role's responsibilities and challenges."
        Feel free to utilize these updated versions of the role description and prompt to effectively communicate the emphasis on testing the problem-handling skills of the candidate.
        Also Create an expected profound answer to the question which can later be used for scoring candidate's response.
        Keep the situation to a one to two liner response ie not a much broader answered situation.
        Please provide your response inside a dictionary with keys exactly same of the following format:('problem_statement(contains the problem statement)', 'expected_answer')
    """

def analyse_situational_answer(situation,expected_answer,candidate_answer):
    return f"""
        Situational Question
        {situation}

        Expected Answer
        {expected_answer}

        Candidate Answer
        {candidate_answer}

        Given the Situational Question and expected answer provided, please evaluate the candidate answer to the  situational question that assesses a candidate's problem-handling skills and response to a relevant work scenario. 
        Feel free to utilize these updated versions of the role description and prompt to effectively communicate the emphasis on testing the problem-handling skills of the candidate.
        Also Create an expected profound score out of 10 to the question which can later be used for scoring candidate's response.
        Please provide your response inside a dictionary with keys exactly same of the following format:('score')
    """



    
