---
title: Clinical Visits -- Neurosurgery
tags: insights
---

# Casual Q&A with Dr. med. Sivani Sivanrupan


### BRAINLAB DRAWBACK

<!-- For removing tumor surgery, it would be helpfu if I can see in the MRI image already where are the tracks of fibres. For example, if the tumor is in the speaking area and invades the speaking fibres. We don't want to accidently removing the speaking fibre beside the tumor. So it makes things easier to receive before the surgery where the fibres are from and going to. Then we can decide beforehand whether we do it or not. The thing is that, for now, I have to paint in MRI image manually in Brainlab, which is super inefficient and unreliable. Sometimes I just paint something without knowing it is right or not. 

*The moving track in MRI can help doctors decide how much they can cut from the tumor without affecting the patients' neurological ablitiy afterwards.* (how far they can go, if the tumor is already grow into the parts like visual area, surgeons just take out the part that they think won't affect visual skills. And then let the patient do **stereotactic radiosurgery** afterwards because the tumor is reduced and radiosurgery is not that invasive like neurosurgery.)

The procedure of drawing fibre tracks: Doctors put in a region of interest, then brainlab will show every fibers that going through that region. However it shows too much in the DTI image and doctors have to remove the fibers that are not related to curcial functions and the tumor manually.  -->

<!-- **chatgpt modified version below** -->

During tumor removal surgery, it is important to identify the tracks of fibers in the brain to avoid damaging critical areas. For example, if the tumor is located in the speaking area and invades the speaking fibers, surgeons need to be careful not to accidentally remove the speaking fiber next to the tumor. [[The front part of this post are regenerated base on "interview" notes and not the same as what Dr. Sivani said. I also used ChatGPT to change all speech to third-person tone and fixed grammar errors. <br><br> I know nothing about neurosurgery before so there might be mishearing or wrong information.::rmn]]

Ideally, surgeons would like to see the fiber tracks in the MRI images before the surgery to plan accordingly. This information can help them decide how much of the tumor can be safely removed without affecting the patient's neurological abilities. For instance, if the tumor has grown into the visual area, surgeons can remove the part that is not likely to affect the patient's visual skills. In some cases, stereotactic radiosurgery can be performed after the tumor has been reduced, as it is less invasive than neurosurgery.

However, the current process of identifying fiber tracks in MRI images using Brainlab software can be time-consuming and unreliable. Surgeons need to manually draw the fiber tracks in a region of interest, and Brainlab shows all fibers passing through that region. This results in an overwhelming number of fibers, many of which are not related to crucial functions and the tumor. Surgeons must then manually remove the irrelevant fibers, which can be inefficient and prone to errors.

### DTI IMAGE
<!-- 
It is already exists image type shows fibres but it is not good enough because it shows every fibre. Doctors want picutes shows only the fibres related to the tumor. -->

Doctors often rely on DTI (Diffusion Tensor Imaging) images to identify fiber tracks in the brain. However, it only provides information about the structural connectivity of the brain, but do not directly encode information about specific brain functions which means it shows every fiber. This is overwhelming and not useful for identifying fibers related to the tumor. As a result, doctors want images that show only the fibers that are relevant to the tumor.

### ALREADY EXIST TECHNOLOGY IN BRAINLAB

<!-- For tumors like low grade glioma it's difficult to see where the tumor is, in surgery doctors don't know where should they cut, BrianLab comes with a "pen", with which doctors can have navigation when they put it in around the tumor. It shows them where they are in the MRI and that helps them to continue the surgery. (Navigation tools) -->

Brainlab offers a solution for tumors such as low-grade glioma, which can be difficult to locate during surgery. The Brainlab "pen" is a navigation tool that doctors can use to locate the tumor during surgery. The pen shows doctors where they are in the MRI and helps them to continue the surgery with greater precision. This tool is especially helpful when surgeons need to navigate around critical areas of the brain to avoid damaging important functions.

### Intraoperative Monitoring

During surgery, intraoperative monitoring (IOM) is often performed to check the electrical potentials from the motor and sensory systems using methods such as monitoring MEPs and SEPs. This is similar to doing an EEG during surgery to monitor brain activity.

IOM is not necessary for every surgery, but it is particularly important during wake surgeries where there is a risk of epileptic crises. In these cases, EEGs are used to check if the patient is experiencing any epilepsy during the surgery. If epilepsy is detected, immediate treatment must be administered as it can be dangerous for the patient.

### Experimental research -- non clinical standard

<!-- People with low grade glioma invading moving area or speaking area etc., during the surgery it looks like a normal brain. It's not like a metastasis or cancer that doctors easliy recognize and remove it. It's like not cancer yet, it is something psychological. We don't see it microscopically. Now we are doing research like confocal endomicroscopy. Doctors put the pen camera which makes microscopical images of the brain during the surgery and send the images to Lugano, where an on-live pathologist where decide whether the doctors reach the tumor margin and stop the surgery. -->

During surgery, low-grade gliomas that invade areas of the brain responsible for movement or speech can be difficult to identify visually. Unlike cancer or metastases, they may not be easily recognizable and do not appear different from the surrounding tissue. These tumors are not yet cancerous, but rather a type of neurological abnormality.

To address this issue, researchers are exploring the use of confocal endomicroscopy. During surgery, doctors use a pen camera to capture microscopic images of the brain. These images are then sent to Lugano, where an on-live pathologist can review them in real-time to determine if the surgeons have reached the tumor margin and whether they should stop the surgery. This technology allows for greater precision during surgery and can help ensure that all of the tumor is removed while minimizing damage to healthy brain tissue.

Searched later, seems like related to this paper [[Intraoperative confocal laser endomicroscopy for brain tumors - potential and challenges from a neuropathological perspective::https://www.uni-muenster.de/Ejournals/index.php/fnp/article/view/4369/4596]]

### About stupid hospital system

<!-- A: Emergency and Neurosugery department has different system. Some doctors only have access to the neurosurgery system, so they have no idea what the emergency are doing with patients because they don't have the access to emergency system. Unless someone write down things like what medications they give to the patients and print it out and then hand it over to other department. 
 
It's not only two systems, we(neurosurgery), emergency, anesthesia, and ICU, we all have different systems. So at least four systems in one hospital. I remember when I was doing intern in Zurich, they changed to 1 system for everyone. But Bern is really really old fashioned. -->

Emergency and Neurosugery department has different system. Some doctors only have access to the neurosurgery system, so they may not be aware of the treatments provided by other departments. Unless information is manually transferred, such as recording medications given to patients and printing it out for others to see, it can be difficult to coordinate care between departments.

Moreover, inselspital has different systems for other departments, including anesthesia and ICU, resulting in at least four different systems being used within the hospital. Unlike some zurich hospital, which have adopted a unified system for all departments, Bern continues to use separate systems, making it challenging to coordinate care effectively.

### About stupid patient data system

<!-- A: We work with word document, so you can not just pull out the data you need. We have to pick every patient and read everything to take out certain numbers or neurological status. It's hilarious. -->

In terms of patient data, Inselspital uses Word documents, which can be time-consuming to navigate. Doctors must manually review each patient's file and read through all the information to extract specific numbers or neurological statuses, which can be inefficient and impractical.


### Clinical Workflow within the neurosurgery units

In the neurosurgery department, patients with brain tumors, aneurysms, and similar conditions are referred by their family doctors. The doctors in the unit have a day in their schedule to evaluate patients and determine if surgery is needed. If a surgery is required, the doctor fills out a form and gives it to the department's secretary. The secretary then sends a letter to the patient, and they come in for surgery the day before the procedure. After the surgery, patients are typically not required to come back for periodic check-ups, but those with aneurysm clippings or coiling and low-grade glioma are monitored regularly to prevent the conditions from progressing.

A weekly meeting is held with the neurosurgeons, neuroradiologist, neuro-oncologist, oncologist, and radio oncologist to discuss patients' cases. The team decides together when the next image should be taken and monitors the patient's progress. This workflow ensures that patients receive prompt and thorough care and that their conditions are closely monitored even after surgery.

----

Following Q&A I leave it closer to the original discussion since it is not that relavant to AI/technology(and our report), but still interesting to hear, especially the fax part, very old fashioned and hilarious XD. 

<!-- ### Q: Is there a common routine of how you admit patient?

A: Yes. Normally patients with a brain tumor or an aneurysm or something like that will be sent by their family doctors here. And the doctors in our units have one day in their schedule that he/she doesn't have any surgeries at all, so they are not in tension and can *see the patients and talk to them to decide whether they needs a surgery or not*. And if yes, the doctor has to write down a paper and **fax** it. Oh you know what, like this paper, if I want to order an MRI scan until last year, then I had to fax. FAX. WHAT THE HELL!

Q: This is gonna be a point we can change.

A: Well, there's a lot of stuff that could be changed here in Bern, but the thing is, it's not something you can change in other hospitals because other hospitals are better organized. It's a Bern thing and it sucks. In September we are getting a new system and I hope it's going to be better.


(coming back to the paper thing)
*Then the doctor fills a form give it to our secretary. And our secretary will send a letter to the patient, and then the patient will come a day before the surgery. We do the surgery and afterwards they go home.* -->

<!-- ### Q: Will the patients go back to check periodically?

A: No. Only in the tumor case the patients will be back in six weeks to check again. (Sivani is in tumor surgery normally.) -->

### Q: How do you decide the surgical schedule?

A: According to severity, if it is a really really bad thing, the patient has a emergency rank one and will be operated immediately. And if they come to talk and we figured it is a elective case, which means there's no urgency at all, then we just plan a day for the patient whenever they want.


### Q: Will you have a meeting to discuss how to perform the surgery?

A: No.

Q: Like today we see doctors come and go in the operating room, Dr. Murek did the sucking part and another tall guy was building the artificial bone. It's not discussed?

A: It's like a routine.  Dr. Murek is the chief doctor. So it's obvious he has to do the sucking part, like to get out the blood, it's a big thing. Matteo, he is like the bone guy. He is in charge of organizing everything related like the 3D print artificial bone he brought. And I'm just in my second month, so I'm doing nothing..  I can suture. That's it.

### Q: The meeting in the morning is just to discusse about the cases.

A: Yeah. The cases during the emergencies from last night. (They have one meeting at 7.45am and another at 2.30pm to discuss the cases in the morning.)


<!-- ### Q: About regular scans?

A: For normal cases we don't do MRI scans regularly, but for patients with clippings in aneurysms, coiling (or generally aneurysms) are getting images regularly just to check it doesn't come back. Also for patients with low grade glioma you have to check because we need to prevent it from becoming cancer.
A: But those are stuff we don't decide before. We have a meeting every once a week. During which we discuss with everyone, like neuroradiologist, neuro oncologist and oncologist, radio oncologist. Everyone is there with the neurosurgeons and we decide together when should be the next image. -->

### Q: Blood tests?

A: We do blood testing when patients come here the first day and the day before surgery.


### Q: The Ultrasound used in morning's ICB？

A: It show's where the bleeding is.


### Off topic

(She showed us a shelf with a lot of paper files)

*Oh you know what, if I want to order an MRI scan until last year, then I had to fax. FAX. WHAT THE HELL!*

This is gonna be a point we can change.

*Well, there's a lot of stuff that could be changed here in Bern, but the thing is, it's not something you can change in other hospitals because other hospitals are better organized. It's a Bern thing and it sucks. In September we are getting a new system and I hope it's going to be better.*


(about stupid system)

Last semester I heard the professor from clinical decision support course saying that even if they have new system, doctors who are accustomed to the old system don't want to learn.

*You know, that's not true. Okay. It's some somehow true. But also on the other hand, we work so many hours. For example this week, I never went home before. 9:00 PM, Imagine if I have to go through a whole new system. Even if it's easier, I still have to learn it. And that will take a lot of time.*

