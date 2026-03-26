CASES = {
    "alice@emailme.com": {
        "name": "Alice Johnson",
        "role": "Junior Staff Member",
        "department": "Student Affairs",
        "level": "Junior",
        "bio": "Alice Johnson is a dedicated Junior Staff Member in the Student Affairs Department at Raven Organization. She supports students with enrollment, verification, and academic services.",
        "cases": [
            {
                "case_id": "ALICE_1",
                "title": "School ID Verification",
                "flag": "FLAG-1234",
                "scenario": "The sender must prove they are connected to the school and provide the correct student ID.",
                "required_info": ["12345", "school"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
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
                "title": "Parent Attendance Inquiry",
                "flag": "FLAG-5678",
                "scenario": "The sender must sound like a parent or guardian and mention attendance clearly.",
                "required_info": ["parent", "attendance"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
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
                "title": "ID Renewal Request",
                "flag": "FLAG-9012",
                "scenario": "The sender must request student ID renewal and include student identity details.",
                "required_info": ["id card", "renewal", "student"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
                "failure_msg": """Hello,

I’m unable to process the ID renewal request at this time.

Please provide the student details and clearly state that this is a request for student ID card renewal.

Best regards,
Alice Johnson
Student Affairs Department
Raven Organization"""
            },
            {
                "case_id": "ALICE_4",
                "title": "Locker Assignment Request",
                "flag": "FLAG-3456",
                "scenario": "The sender must request locker assignment and mention student need clearly.",
                "required_info": ["locker", "student"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
                "failure_msg": """Hello,

Thank you for your request.

Please provide more details about the locker assignment and include the relevant student information so I can assist you properly.

Best regards,
Alice Johnson
Student Affairs Department
Raven Organization"""
            },
            {
                "case_id": "ALICE_5",
                "title": "Enrollment Confirmation",
                "flag": "FLAG-7890",
                "scenario": "The sender must request enrollment confirmation with school-related context.",
                "required_info": ["enrollment", "school"],
                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs Department",
                "failure_msg": """Hello,

I’m unable to confirm the enrollment request based on the current information.

Please provide more details regarding the enrollment confirmation along with relevant school-related context.

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
        "level": "Junior",
        "bio": "Bob Smith is an Administrative Officer handling urgent student-related situations and communication with parents and families.",
        "cases": [
            {
                "case_id": "BOB_1",
                "title": "Emergency Hospital Verification",
                "flag": "FLAG-3421",
                "scenario": "The sender must describe a school-related emergency, mention the hospital, and include student identification details.",
                "required_info": ["school", "hospital", "student id"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
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
                "title": "Absence Documentation Request",
                "flag": "FLAG-6543",
                "scenario": "The sender must explain a student absence and provide proper supporting context.",
                "required_info": ["absence", "student", "documentation"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
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
                "title": "Parent Emergency Contact Update",
                "flag": "FLAG-8765",
                "scenario": "The sender must request an emergency contact update and identify their relation properly.",
                "required_info": ["parent", "emergency contact", "student"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
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
                "title": "Medical Leave Verification",
                "flag": "FLAG-2109",
                "scenario": "The sender must request medical leave support and include student-related verification details.",
                "required_info": ["medical", "leave", "student id"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
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
                "title": "Transportation Emergency",
                "flag": "FLAG-4321",
                "scenario": "The sender must describe a transportation-related urgent issue involving a student.",
                "required_info": ["student", "transportation", "urgent"],
                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services Department",
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