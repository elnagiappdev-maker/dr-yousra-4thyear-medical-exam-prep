import streamlit as st
import json
import pandas as pd
from datetime import datetime
import os

# Set page config
st.set_page_config(
    page_title="4th Year Medical Exam Prep",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .question-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .correct-answer {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .incorrect-answer {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .footer {
        text-align: center;
        color: #666;
        font-size: 12px;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #ddd;
    }
    .copyright {
        text-align: center;
        color: #999;
        font-size: 11px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load questions data
@st.cache_data
def load_questions():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'questions_database.json')
    with open(json_path, 'r') as f:
        return json.load(f)

questions_data = load_questions()

# Initialize session state
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = None
if 'show_explanation' not in st.session_state:
    st.session_state.show_explanation = False
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'current_mode' not in st.session_state:
    st.session_state.current_mode = 'home'
if 'selected_system' not in st.session_state:
    st.session_state.selected_system = None
if 'selected_type' not in st.session_state:
    st.session_state.selected_type = None

# Sidebar
with st.sidebar:
    st.title("📚 Navigation")
    page = st.radio("Select Page", ["Home", "Questions", "Study Notes", "Progress", "About"])

# Main content
if page == "Home":
    st.markdown('<div class="main-header"><h1>Master Your 4th Year Medical Exams</h1></div>', unsafe_allow_html=True)
    
    st.write("Comprehensive question bank with 120+ high-quality questions designed to UK and USA exam standards.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Questions", "123")
    with col2:
        st.metric("Question Types", "3")
    with col3:
        st.metric("Medical Systems", "6")
    with col4:
        st.metric("Study Notes", "24")
    
    st.markdown("---")
    
    st.subheader("📖 Question Types")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("### SBA (Single Best Answer)")
        st.write(f"**60 questions**")
        st.write("Single best answer questions with detailed explanations for both correct and incorrect options.")
    
    with col2:
        st.write("### MCQ (Multiple Choice)")
        st.write(f"**60 questions**")
        st.write("Multiple choice questions covering all major topics across medical systems.")
    
    with col3:
        st.write("### EMQ (Extended Match)")
        st.write(f"**3 question sets**")
        st.write("Extended match questions testing clinical reasoning and decision-making.")
    
    st.markdown("---")
    
    st.subheader("🏥 Medical Systems Covered")
    
    systems = ["Renal", "CNS", "Musculoskeletal", "Reproductive", "Cardiovascular", "Respiratory"]
    cols = st.columns(3)
    
    for idx, system in enumerate(systems):
        with cols[idx % 3]:
            st.write(f"✓ {system}")
    
    st.markdown("---")
    
    st.subheader("Why Choose Our Question Bank?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**UK & USA Standards**")
        st.write("Questions designed to match the difficulty and format of UK and USA medical exams.")
    
    with col2:
        st.write("**Detailed Explanations**")
        st.write("Every question includes comprehensive explanations for both correct and incorrect answers.")
    
    with col3:
        st.write("**Progress Tracking**")
        st.write("Track your performance and identify weak areas for targeted revision.")
    
    # Footer
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Medical Content Developed By:")
    st.markdown("**Dr. Yousra Abdelatti**")
    st.markdown("**Dr. Mohammedelnagi Mohammed**")
    st.markdown('<div class="copyright">© 2025 4th Year Medical Exam Prep. All rights reserved.<br>All rights reserved to Dr. Yousra Abdelatti and Dr. Mohammedelnagi Mohammed.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Questions":
    st.title("📝 Question Bank")
    
    # Filters
    col1, col2 = st.columns(2)
    
    with col1:
        question_type = st.selectbox(
            "Select Question Type",
            ["All", "SBA", "MCQ", "EMQ"],
            key="question_type_select"
        )
    
    with col2:
        system = st.selectbox(
            "Select Medical System",
            ["All", "Renal", "CNS", "Musculoskeletal", "Reproductive", "Cardiovascular", "Respiratory"],
            key="system_select"
        )
    
    # Get filtered questions
    all_questions = []
    
    if question_type in ["All", "SBA"]:
        all_questions.extend([(q, "SBA") for q in questions_data.get("sba", [])])
    if question_type in ["All", "MCQ"]:
        all_questions.extend([(q, "MCQ") for q in questions_data.get("mcq", [])])
    if question_type in ["All", "EMQ"]:
        all_questions.extend([(q, "EMQ") for q in questions_data.get("emq", [])])
    
    # Filter by system
    if system != "All":
        all_questions = [(q, qtype) for q, qtype in all_questions if q.get("system") == system]
    
    if not all_questions:
        st.warning("No questions found for the selected filters.")
    else:
        st.info(f"Found {len(all_questions)} question(s)")
        
        # Display questions
        for idx, (question, qtype) in enumerate(all_questions):
            with st.container():
                st.markdown(f'<div class="question-container">', unsafe_allow_html=True)
                
                st.markdown(f"### Question {idx + 1} ({qtype}) - {question.get('system', 'Unknown')}")
                st.write(question.get("question", ""))
                
                # Display options
                if qtype in ["SBA", "MCQ"]:
                    options = question.get("options", [])
                    selected = st.radio(
                        "Select your answer:",
                        options=range(len(options)),
                        format_func=lambda x: f"{chr(65+x)}: {options[x]}",
                        key=f"answer_{question.get('id')}"
                    )
                    
                    if st.button("Submit Answer", key=f"submit_{question.get('id')}"):
                        correct_answer = question.get("correct_answer", "")
                        user_answer = chr(65 + selected)
                        
                        if user_answer == correct_answer:
                            st.markdown(
                                f'<div class="correct-answer"><strong>✓ Correct!</strong><br>{question.get("explanation_correct", "")}</div>',
                                unsafe_allow_html=True
                            )
                        else:
                            st.markdown(
                                f'<div class="incorrect-answer"><strong>✗ Incorrect</strong><br><strong>Correct Answer:</strong> {correct_answer}<br><strong>Explanation:</strong> {question.get("explanation_incorrect", "")}</div>',
                                unsafe_allow_html=True
                            )
                
                elif qtype == "EMQ":
                    st.write("**Cases:**")
                    for case_idx, case in enumerate(question.get("cases", [])):
                        st.write(f"{case_idx + 1}. {case.get('case', '')}")
                        selected = st.selectbox(
                            f"Answer for case {case_idx + 1}:",
                            options=question.get("options", []),
                            key=f"emq_answer_{question.get('id')}_{case_idx}"
                        )
                        
                        if st.button("Check Answer", key=f"emq_submit_{question.get('id')}_{case_idx}"):
                            if selected == question.get("options", [])[ord(case.get("answer", "A")) - 65]:
                                st.markdown(
                                    f'<div class="correct-answer"><strong>✓ Correct!</strong><br>{case.get("explanation", "")}</div>',
                                    unsafe_allow_html=True
                                )
                            else:
                                st.markdown(
                                    f'<div class="incorrect-answer"><strong>✗ Incorrect</strong><br>{case.get("explanation", "")}</div>',
                                    unsafe_allow_html=True
                                )
                
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("---")

elif page == "Study Notes":
    st.title("📖 Study Notes")
    
    system = st.selectbox(
        "Select Medical System",
        ["All", "Renal", "CNS", "Musculoskeletal", "Reproductive", "Cardiovascular", "Respiratory"]
    )
    
    notes = questions_data.get("shortNotes", [])
    
    if system != "All":
        notes = [n for n in notes if n.get("system") == system]
    
    if not notes:
        st.warning("No study notes found for the selected system.")
    else:
        for note in notes:
            with st.expander(f"📝 {note.get('title', '')} - {note.get('system', '')}"):
                st.write(note.get("content", ""))

elif page == "Progress":
    st.title("📊 Your Progress")
    
    st.info("Progress tracking features coming soon! This feature will track your question attempts and performance metrics.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Questions Attempted", "0")
    with col2:
        st.metric("Correct Answers", "0")
    with col3:
        st.metric("Success Rate", "0%")
    
    st.markdown("---")
    st.subheader("Performance by System")
    
    systems = ["Renal", "CNS", "Musculoskeletal", "Reproductive", "Cardiovascular", "Respiratory"]
    
    # Create sample data for visualization
    data = {
        "System": systems,
        "Attempted": [0] * len(systems),
        "Correct": [0] * len(systems),
        "Percentage": [0] * len(systems)
    }
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

elif page == "About":
    st.title("ℹ️ About This Platform")
    
    st.write("""
    ### 4th Year Medical Exam Preparation Platform
    
    This comprehensive question bank is designed specifically for 4th year medical students preparing for distinction-level exams.
    
    #### Content Overview
    
    - **123 High-Quality Questions** across 6 major medical systems
    - **60 SBA (Single Best Answer)** questions with detailed explanations
    - **60 MCQ (Multiple Choice)** questions with answer keys
    - **3 EMQ (Extended Match)** question sets with clinical scenarios
    - **24 Study Notes** covering key topics for revision
    
    #### Medical Systems Covered
    
    1. **Renal** - Kidney disease, acute kidney injury, glomerulonephritis
    2. **CNS** - Neurological disorders, stroke, epilepsy
    3. **Musculoskeletal** - Bone disease, arthritis, trauma
    4. **Reproductive** - Obstetrics, gynecology, sexual health
    5. **Cardiovascular** - Heart disease, hypertension, arrhythmias
    6. **Respiratory** - Lung disease, asthma, COPD
    
    #### Question Standards
    
    All questions are designed to match the difficulty and format of:
    - **UK Medical Exams** (MRCP, FRCP, etc.)
    - **USA Medical Exams** (USMLE, ABIM, etc.)
    - **International Medical Exams** (PLAB, etc.)
    
    #### Features
    
    ✓ Detailed explanations for both correct and incorrect answers
    ✓ Filtering by medical system and question type
    ✓ Progress tracking and performance analytics
    ✓ Study notes for quick revision
    ✓ Mobile-friendly interface
    
    """)
    
    st.markdown("---")
    
    st.subheader("Medical Content Developed By:")
    st.write("**Dr. Yousra Abdelatti**")
    st.write("**Dr. Mohammedelnagi Mohammed**")
    
    st.markdown("---")
    
    st.markdown("""
    <div class="copyright">
    © 2025 4th Year Medical Exam Prep. All rights reserved.<br>
    All rights reserved to Dr. Yousra Abdelatti and Dr. Mohammedelnagi Mohammed.<br>
    <br>
    Designed for 4th year medical students seeking distinction in medical exams.<br>
    Made with ❤️ for medical education.
    </div>
    """, unsafe_allow_html=True)

# Footer on all pages
st.markdown("---")
st.markdown("""
<div class="copyright" style="margin-top: 30px;">
© 2025 4th Year Medical Exam Prep. All rights reserved to Dr. Yousra Abdelatti and Dr. Mohammedelnagi Mohammed.
</div>
""", unsafe_allow_html=True)
