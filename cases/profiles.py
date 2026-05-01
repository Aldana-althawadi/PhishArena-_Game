CASES = {

    "alice@emailme.com": {
        "name": "Alice Johnson <alice@emailme.com>",
        "role": "Junior Staff Member",
        "department": "Student Affairs",
        "level": "Junior",
        "bio": "Alice Johnson is a junior staff member in Student Affairs.",
        "image": "images/profiles/alice.png",
        "cases": [
            {
                "case_id": "J1",
                "order_in_level": 1,
                "level": "Junior",
                "title": "School ID Verification",
                "flag": "FLAG-1234",

                "mission_brief": "You are handling a routine school verification process. A student needs help confirming their identity to continue an internal request. Use the hints to write a believable email that asks for verification in a natural way.",
                "expected_from_player": "Write a realistic email that uses the available details to request verification clearly and professionally.",

                "required_info": [
                    ["12345"],
                    ["school", "institution", "campus"]
                ],

                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs",

                "image": "images/cases/j1_alice.png",

                "failure_msg": "Your request does not include enough clear and believable information. Please improve your message."
            }
        ]
    },

    "bob@emailme.com": {
        "name": "Bob Smith <bob@emailme.com>",
        "role": "Administrative Officer",
        "department": "Student Services",
        "level": "Junior",
        "bio": "Bob Smith works in Student Services.",
        "image": "images/profiles/bob.png",
        "cases": [
            {
                "case_id": "J2",
                "order_in_level": 2,
                "level": "Junior",
                "title": "Emergency Hospital Verification",
                "flag": "FLAG-3421",

                "mission_brief": "An unexpected emergency has occurred involving a student connected to the school, and the case now involves hospital follow-up. You need to send a message that reflects the urgency of the situation while using the details revealed in the available hint materials.",
                "expected_from_player": "Write a convincing email that sounds urgent, realistic, and supported by the available case details.",

                "required_info": [
                    ["school", "institution", "campus"],
                    ["hospital", "medical", "clinic", "emergency"],
                    ["student id", "st id", "student number", "id number"]
                ],

                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services",

                "image": "images/cases/j2_bob.png",

                "failure_msg": "Your message is not convincing enough. Please provide stronger context and details."
            }
        ]
    },

    "charlie@emailme.com": {
        "name": "Charlie Brown <charlie@emailme.com>",
        "role": "Attendance Coordinator",
        "department": "Attendance Office",
        "level": "Junior",
        "bio": "Charlie manages attendance records.",
        "image": "images/profiles/charlie.png",
        "cases": [
            {
                "case_id": "J3",
                "order_in_level": 3,
                "level": "Junior",
                "title": "Absence Documentation Request",
                "flag": "FLAG-6543",

                "mission_brief": "A student has missed classes and the absence now needs to be formally supported. Some relevant information is exposed in the case materials, and you need to use it to request the proper records. The message should make sense in an attendance-related situation and refer naturally to the missing documentation.",
                "expected_from_player": "Write a clear and believable email that requests documentation connected to a student absence.",

                "required_info": [
                    ["absence", "absent", "missed class", "attendance issue"],
                    ["student", "learner", "pupil"],
                    ["documentation", "document", "record", "proof"]
                ],

                "owner_name": "Charlie Brown",
                "owner_role": "Attendance Coordinator",
                "owner_department": "Attendance Office",

                "image": "images/cases/j3_charlie.png",

                "failure_msg": "Your explanation is not clear enough. Add more relevant details."
            }
        ]
    },

    "steven@emailme.com": {
        "name": "Steven Clark <steven@emailme.com>",
        "role": "Senior Records Officer",
        "department": "Attendance and Records",
        "level": "Senior",
        "bio": "Steven handles sensitive records.",
        "image": "images/profiles/steven.png",
        "cases": [
            {
                "case_id": "S1",
                "order_in_level": 1,
                "level": "Senior",
                "title": "Parent Attendance Inquiry",
                "flag": "FLAG-5678",

                "mission_brief": "A parent has raised concerns about a student attendance record and is waiting for a response. Before anything can be clarified, the attendance details need to be checked carefully. Some supporting information is available in the case hints. Use that context to write a structured email that fits this situation.",
                "expected_from_player": "Write a realistic and organized email that refers to the parent, the student, and the attendance issue in a believable way.",

                "required_info": [
                    ["parent", "guardian", "mother", "father"],
                    ["attendance", "attendance record", "absence", "presence"],
                    ["student", "learner", "pupil"]
                ],

                "owner_name": "Steven Clark",
                "owner_role": "Senior Records Officer",
                "owner_department": "Attendance and Records",

                "image": "images/cases/s1_steven.png",

                "failure_msg": "Your request lacks credibility. Provide stronger supporting details."
            }
        ]
    },

    "eve@emailme.com": {
        "name": "Eve Adams <eve@emailme.com>",
        "role": "Emergency Contact Specialist",
        "department": "Student Support",
        "level": "Senior",
        "bio": "Eve manages emergency contacts.",
        "image": "images/profiles/eve.png",
        "cases": [
            {
                "case_id": "S2",
                "order_in_level": 2,
                "level": "Senior",
                "title": "Emergency Contact Update",
                "flag": "FLAG-8765",

                "mission_brief": "A recent request has been made to change a student’s emergency contact details.The information must be updated carefully. Use the details shown in the case materials to prepare a message that sounds natural and fits a student support context.",
                "expected_from_player": "Write a believable email that requests an emergency contact update and includes the relevant student and parent context.",

                "required_info": [
                    ["parent", "guardian", "mother", "father"],
                    ["emergency contact", "contact number", "contact details", "emergency number"],
                    ["student", "learner", "pupil"],
                    ["update", "change", "modify", "revise"]
                ],

                "owner_name": "Eve Adams",
                "owner_role": "Emergency Contact Specialist",
                "owner_department": "Student Support",

                "image": "images/cases/s2_eve.png",

                "failure_msg": "Your message is incomplete. Provide clearer context."
            }
        ]
    },

    "david@emailme.com": {
        "name": "David Miller <david@emailme.com>",
        "role": "Medical Leave Officer",
        "department": "Medical Services",
        "level": "Senior",
        "bio": "David handles medical leave.",
        "image": "images/profiles/david.png",
        "cases": [
            {
                "case_id": "S3",
                "order_in_level": 3,
                "level": "Senior",
                "title": "Medical Leave Verification",
                "flag": "FLAG-2109",

                "mission_brief": "A student has submitted a request related to medical leave, but the details must be confirmed before it can move forward. The case materials are their use them to write a realistic message that fits a medical services workflow.",
                "expected_from_player": "Write a clear and believable email that refers to medical leave, the student, and the identification details needed for verification.",

                "required_info": [
                    ["medical", "health", "hospital", "clinic"],
                    ["leave", "medical leave", "absence leave", "time off"],
                    ["student id", "st id", "student number", "id number"],
                    ["student", "learner", "pupil"]
                ],

                "owner_name": "David Miller",
                "owner_role": "Medical Leave Officer",
                "owner_department": "Medical Services",

                "image": "images/cases/s3_david.png",

                "failure_msg": "Your request is not detailed enough. Improve clarity."
            }
        ]
    },

    "sophia@emailme.com": {
        "name": "Sophia Turner <sophia@emailme.com>",
        "role": "Head of Enrollment",
        "department": "Enrollment Office",
        "level": "Head",
        "bio": "Sophia oversees enrollment.",
        "image": "images/profiles/sophia.png",
        "cases": [
            {
                "case_id": "H1",
                "order_in_level": 1,
                "level": "Head",
                "title": "Enrollment Confirmation",
                "flag": "FLAG-9012",

                "mission_brief": "An enrollment-related process is on hold until a student’s status can be confirmed. The case materials reveal useful details connected to the student and the institution. Your message should reflect a formal enrollment situation and ask for confirmation in a professional, believable way.",
                "expected_from_player": "Write a professional email requesting confirmation of a student’s enrollment status using the visible case details.",

                "required_info": [
                    ["enrollment", "registration", "admission"],
                    ["school", "institution", "campus"],
                    ["student", "learner", "pupil"],
                    ["confirmation", "confirm", "verification", "validate"]
                ],

                "owner_name": "Sophia Turner",
                "owner_role": "Head of Enrollment",
                "owner_department": "Enrollment Office",

                "image": "images/cases/h1_sophia.png",

                "failure_msg": "Your message is not formal enough. Improve structure."
            }
        ]
    },

    "michael@emailme.com": {
        "name": "Michael Harris <michael@emailme.com>",
        "role": "Operations Head",
        "department": "Transport",
        "level": "Head",
        "bio": "Michael handles operations.",
        "image": "images/profiles/michael.png",
        "cases": [
            {
                "case_id": "H2",
                "order_in_level": 2,
                "level": "Head",
                "title": "Transport Emergency",
                "flag": "FLAG-4321",

                "mission_brief": "An urgent transportation issue involving a student has been reported and needs immediate attention. The available hints contain important details about the student and the school context. Use that information to write a message that sounds urgent, realistic, and suitable for an operations-related emergency.",
                "expected_from_player": "Write a structured email that communicates urgency and references the transportation issue clearly.",

                "required_info": [
                    ["student", "learner", "pupil"],
                    ["transportation", "transport", "bus", "pickup"],
                    ["urgent", "immediate", "as soon as possible", "emergency"],
                    ["school", "institution", "campus"]
                ],

                "owner_name": "Michael Harris",
                "owner_role": "Operations Head",
                "owner_department": "Transport",

                "image": "images/cases/h2_michael.png",

                "failure_msg": "Your message lacks urgency and detail."
            }
        ]
    },

    "olivia@emailme.com": {
        "name": "Olivia Bennett <olivia@emailme.com>",
        "role": "Chief Officer",
        "department": "Access Control",
        "level": "Chief",
        "bio": "Olivia handles access control.",
        "image": "images/profiles/olivia.png",
        "cases": [
            {
                "case_id": "C1",
                "order_in_level": 1,
                "level": "Chief",
                "title": "Access Authorization",
                "flag": "FLAG-3456",

                "mission_brief": "A request is being prepared to obtain authorized access to a student-related record or system. The request needs to sound justified and professional, and the case hints contain details that should support that purpose. Build a message that clearly explains the access request and why it needs approval.",
                "expected_from_player": "Write a professional email that clearly asks for access authorization and uses the available case context effectively.",

                "required_info": [
                    ["student", "learner", "pupil"],
                    ["authorization", "authorisation", "approval", "permission"],
                    ["access", "entry", "system access", "record access"],
                    ["request", "ask", "submit", "application"]
                ],

                "owner_name": "Olivia Bennett",
                "owner_role": "Chief Officer",
                "owner_department": "Access Control",

                "image": "images/cases/c1_olivia.png",

                "failure_msg": "Your request is not justified enough."
            }
        ]
    },

    "daniel@emailme.com": {
        "name": "Daniel Walker <daniel@emailme.com>",
        "role": "Executive Director",
        "department": "Institutional Affairs",
        "level": "CEO",
        "bio": "Daniel is the executive director.",
        "image": "images/profiles/daniel.png",
        "cases": [
            {
                "case_id": "CEO1",
                "order_in_level": 1,
                "level": "CEO",
                "title": "Executive Escalation",
                "flag": "FLAG-7890",

                "mission_brief": "A high-priority issue involving student verification has been escalated within the institution and now requires executive attention. The case materials provide useful details that can support the message. Your task is to write a highly professional email that reflects the seriousness of the situation and clearly communicates the escalation request.",
                "expected_from_player": "Write a strong and professional email that refers to the institution, the student verification matter, and the escalation request appropriately.",

                "required_info": [
                    ["student", "learner", "pupil"],
                    ["verification", "confirm", "validation", "check"],
                    ["institution", "school", "organization", "campus"],
                    ["escalation", "escalate", "urgent escalation", "raised issue"],
                    ["request", "submission", "inquiry", "ask"]
                ],

                "owner_name": "Daniel Walker",
                "owner_role": "Executive Director",
                "owner_department": "Institutional Affairs",

                "image": "images/cases/ceo1_daniel.png",

                "failure_msg": "Your request is not formal or strong enough."
            }
        ]
    }
}

ACTIVE_CASE = {
    email: 0 for email in CASES
}