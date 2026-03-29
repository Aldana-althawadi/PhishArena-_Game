CASES = {
    "alice@emailme.com": {
        "name": "Alice Johnson",
        "role": "Junior Staff Member",
        "department": "Student Affairs",
        "level": "Mixed",
        "bio": "Alice Johnson is a dedicated Junior Staff Member in the Student Affairs Department at Raven Organization. She supports students with enrollment, verification, and academic services.",
        "cases": [
            {
                "case_id": "ALICE_1",
                "level": "Junior",
                "title": "School ID Verification",
                "flag": "FLAG-1234",
                "scenario": "The sender must prove they are connected to the school and provide the correct student ID.",
                "required_info": ["12345", "school"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
                "image_prompt": "A realistic school administration help desk with a female junior staff member reviewing student verification documents, modern office, calm academic environment, dark blue UI-friendly style",
                "failure_msg": """Hello,

I’m unable to verify your request at the moment.

Please provide your school ID and clearly explain your relation to the school so I can proceed with the verification.

Best regards,
Alice Johnson
Student Affairs Department
Raven Organization"""
            },
            {
                "case_id": "ALICE_2",
                "level": "Senior",
                "title": "Parent Attendance Inquiry",
                "flag": "FLAG-5678",
                "scenario": "The sender must sound like a parent or guardian, mention attendance clearly, and provide enough context to justify the request.",
                "required_info": ["parent", "attendance", "student"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
                "image_prompt": "A realistic parent communication scene in a school office, attendance records on a monitor, female staff member handling an inquiry, professional academic setting, cinematic dark blue and purple tones",
                "failure_msg": """Hello,

Thank you for your message.

To assist you with this request, please clarify your relation to the student and provide more details regarding the attendance inquiry.

Best regards,
Alice Johnson
Student Affairs Department
Raven Organization"""
            },
            {
                "case_id": "ALICE_3",
                "level": "Head",
                "title": "Enrollment Confirmation Request",
                "flag": "FLAG-9012",
                "scenario": "The sender must request enrollment confirmation with school-related context, student identity, and a legitimate reason for needing the confirmation.",
                "required_info": ["enrollment", "school", "student", "confirmation"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
                "image_prompt": "A formal enrollment office scene with student records, school confirmation documents, female administrator at desk, polished academic administration interior, moody blue neon accents",
                "failure_msg": """Hello,

I’m unable to confirm the enrollment request based on the current information.

Please provide more details regarding the enrollment confirmation along with relevant school-related context and student information.

Best regards,
Alice Johnson
Student Affairs Department
Raven Organization"""
            },
            {
                "case_id": "ALICE_4",
                "level": "Chief",
                "title": "Special Access Authorization",
                "flag": "FLAG-3456",
                "scenario": "The sender must request special administrative access using a formal tone, identify the student clearly, and justify the request in a professional manner.",
                "required_info": ["student", "authorization", "access", "request"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
                "image_prompt": "A high-security academic records office, restricted access authorization forms, female staff member verifying a formal request, professional dark interface aesthetic, blue and violet lighting",
                "failure_msg": """Hello,

Thank you for your request.

I’m unable to proceed with this authorization request at the moment. Please provide a clear formal request including the student details and the reason access is required.

Best regards,
Alice Johnson
Student Affairs Department
Raven Organization"""
            },
            {
                "case_id": "ALICE_5",
                "level": "CEO",
                "title": "Executive Verification Escalation",
                "flag": "FLAG-7890",
                "scenario": "The sender must submit a highly formal escalation request containing student context, institutional purpose, explicit verification wording, and a strong professional justification.",
                "required_info": ["student", "verification", "institution", "escalation", "request"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
                "image_prompt": "An executive education administration scene, formal escalation document on screen, institutional verification office, elegant dark futuristic corporate-academic style, intense blue-purple glow",
                "failure_msg": """Hello,

I’m unable to escalate this request based on the current information.

Please provide a formal institutional verification request with clear student context, the purpose of the escalation, and all necessary supporting details.

Best regards,
Alice Johnson
Student Affairs Department
Raven Organization"""
            }
        ]
    },

    "bob@emailme.com": {
        "name": "Bob Smith",
        "role": "Administrative Officer",
        "department": "Student Services",
        "level": "Mixed",
        "bio": "Bob Smith is an Administrative Officer handling urgent student-related situations and communication with parents and families.",
        "cases": [
            {
                "case_id": "BOB_1",
                "level": "Junior",
                "title": "Emergency Hospital Verification",
                "flag": "FLAG-3421",
                "scenario": "The sender must describe a school-related emergency, mention the hospital, and include student identification details.",
                "required_info": ["school", "hospital", "student id"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
                "image_prompt": "A school emergency coordination desk, hospital notification on screen, male administrative officer handling urgent student case, realistic office, dark blue challenge-game style",
                "failure_msg": """Hello,

I understand the urgency of the situation.

However, I’m unable to verify this request at the moment. Please provide the student ID and additional details so I can confirm the information.

Best regards,
Bob Smith
Student Services Department
Raven Organization"""
            },
            {
                "case_id": "BOB_2",
                "level": "Junior",
                "title": "Absence Documentation Request",
                "flag": "FLAG-6543",
                "scenario": "The sender must explain a student absence and provide proper supporting context.",
                "required_info": ["absence", "student", "documentation"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
                "image_prompt": "A student services office with absence forms and documentation review, male officer handling attendance and leave records, realistic school administration scene, dark neon accent style",
                "failure_msg": """Hello,

Thank you for your message.

Please provide a clear explanation of the student's absence along with the required supporting documentation so I can assist further.

Best regards,
Bob Smith
Student Services Department
Raven Organization"""
            },
            {
                "case_id": "BOB_3",
                "level": "Senior",
                "title": "Parent Emergency Contact Update",
                "flag": "FLAG-8765",
                "scenario": "The sender must request an emergency contact update, identify their relation properly, and provide enough context to justify the update.",
                "required_info": ["parent", "emergency contact", "student", "update"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
                "image_prompt": "A family emergency contact update scene in a school administration office, secure records dashboard, male officer reviewing parent request, cinematic blue-purple lighting",
                "failure_msg": """Hello,

I’m unable to process this request at the moment.

Please confirm your relation to the student and provide more details regarding the emergency contact update.

Best regards,
Bob Smith
Student Services Department
Raven Organization"""
            },
            {
                "case_id": "BOB_4",
                "level": "Senior",
                "title": "Medical Leave Verification",
                "flag": "FLAG-2109",
                "scenario": "The sender must request medical leave support and include student-related verification details and a clear medical context.",
                "required_info": ["medical", "leave", "student id", "student"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
                "image_prompt": "A student medical leave review scene, healthcare-related paperwork on desk, male school administrator processing a sensitive request, dark atmospheric interface style",
                "failure_msg": """Hello,

Thank you for your request.

Please provide the student ID and additional details regarding the medical leave so I can verify and process it accordingly.

Best regards,
Bob Smith
Student Services Department
Raven Organization"""
            },
            {
                "case_id": "BOB_5",
                "level": "Head",
                "title": "Transportation Emergency Coordination",
                "flag": "FLAG-4321",
                "scenario": "The sender must describe a transportation-related urgent issue involving a student and provide enough detail for the request to be taken seriously.",
                "required_info": ["student", "transportation", "urgent", "school"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
                "image_prompt": "A high-priority student transportation issue in a school operations office, emergency coordination board, male officer managing transport incident, dark futuristic blue visual style",
                "failure_msg": """Hello,

I understand this may be urgent.

Please provide more detailed information about the transportation issue and include the student details so I can assist you properly.

Best regards,
Bob Smith
Student Services Department
Raven Organization"""
            }
        ]
    }
}


ACTIVE_CASE = {
    "alice@emailme.com": 0,
    "bob@emailme.com": 0
}