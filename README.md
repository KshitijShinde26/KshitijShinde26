<div align="center">

# ☕ Hi, I'm Kshitij Shinde

### **Java Backend Developer | Third Year IT Engineering Student**
*Engineering practical backend systems, scalable REST APIs, relational schemas, and secure server-side architectures.*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KshitijShinde26)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kshitijshinde26/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/kshitu_26/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kshitij26gs@gmail.com)
[![Portfolio](https://img.shields.io/badge/Live_Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://portfolio-delta-six-46.vercel.app)

<br/>

</div>

---

## 📌 About Me

```ini
[STATUS]        🎓 Third Year B.E. in Information Technology Student
[CORE FOCUS]    ☕ Java Backend Development & RESTful API Architecture
[FLAGSHIP]      🚀 Real-Time Surplus Food Marketplace REST Platform
[ALGORITHMS]    💻 Active Problem Solving & Data Structures in Java
[SECURITY]      🔐 Stateless JWT Filter Chains & Role-Based Access Control (RBAC)
[PERSISTENCE]   🗄️ Relational Data Modeling, Spring Data JPA & Hibernate ORM
```

> I focus on building resilient server-side applications using **Java** and the **Spring Ecosystem**. My work centers around architecting clean REST APIs, handling database transactions with JPA/Hibernate, implementing token-based security filter chains, and solving algorithmic problems with Java.

---

## ☕ Java Backend Development Stack

<div align="center">

| Area | Technologies & Frameworks |
| :--- | :--- |
| **Language & Core** | ![Java](https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Core Java](https://img.shields.io/badge/Core_Java_OOP-ED8B00?style=flat-square&logoColor=white) ![Collections](https://img.shields.io/badge/Collections_&_Generics-ED8B00?style=flat-square&logoColor=white) |
| **Backend Frameworks** | ![Spring Boot](https://img.shields.io/badge/Spring_Boot_3.3.5-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![Spring MVC](https://img.shields.io/badge/Spring_MVC-6DB33F?style=flat-square&logo=spring&logoColor=white) ![REST APIs](https://img.shields.io/badge/RESTful_APIs-0052CC?style=flat-square&logoColor=white) |
| **Security & Auth** | ![Spring Security](https://img.shields.io/badge/Spring_Security_6-6DB33F?style=flat-square&logo=springsecurity&logoColor=white) ![JWT](https://img.shields.io/badge/Stateless_JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white) ![RBAC](https://img.shields.io/badge/Role_Based_Access_Control-4B0082?style=flat-square&logoColor=white) |
| **Database & Persistence** | ![Spring Data JPA](https://img.shields.io/badge/Spring_Data_JPA-59666C?style=flat-square&logo=hibernate&logoColor=white) ![Hibernate](https://img.shields.io/badge/Hibernate_ORM-59666C?style=flat-square&logo=hibernate&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL_InnoDB-4479A1?style=flat-square&logo=mysql&logoColor=white) ![HikariCP](https://img.shields.io/badge/HikariCP-003B57?style=flat-square&logoColor=white) |
| **Messaging & Events** | ![WebSockets](https://img.shields.io/badge/WebSockets_STOMP-010101?style=flat-square&logo=socketdotio&logoColor=white) ![Spring Events](https://img.shields.io/badge/ApplicationEventPublisher-6DB33F?style=flat-square&logo=spring&logoColor=white) |
| **DTOs & Validation** | ![Jakarta Validation](https://img.shields.io/badge/Jakarta_Validation_JSR--380-107C41?style=flat-square&logoColor=white) ![MapStruct](https://img.shields.io/badge/MapStruct_Mappers-E58C3A?style=flat-square&logoColor=white) |
| **Build & Tooling** | ![Apache Maven](https://img.shields.io/badge/Apache_Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white) |

</div>

---

## 🚀 Featured Project

### 🛒 [Surplus Food Marketplace Backend](https://github.com/KshitijShinde26/Surplus_Food_MarketPlace_Project)
> **An enterprise-grade Java REST API platform designed to connect commercial food businesses with consumers and NGOs, facilitating surplus food commerce and donation redistribution.**

```text
HTTP / WebSocket Requests
          │
          ▼
[ Spring Security Filter Chain ] ──► Stateless JWT Auth & SecurityContext (RBAC)
          │
          ▼
[ DispatcherServlet & Spring MVC ] ──► JSR-380 Input Validation & Endpoint Routing
          │
          ▼
[ Service & Business Logic Tier ] ──► MapStruct Entity/DTO Mapping & Event Dispatch
          │
          ├──► [ Real-Time Notifications ] ──► Spring WebSocket & STOMP Message Broker
          └──► [ Persistence Layer ] ──► Spring Data JPA & Hibernate ORM (HikariCP)
                     │
                     ▼
              [ MySQL Database ] ──► InnoDB Engine (ACID Transactions & Constraints)
```

#### 🔑 Key Backend Functionality:
- **Backend Architecture:** Modular layered design built with **Java 21** and **Spring Boot 3.3.5** (Controllers, Services, Repositories, Entities, DTOs, Mappers).
- **Stateless JWT Security:** Custom `JwtAuthenticationFilter` verifying bearer tokens, maintaining security context, and enforcing role authorization (`ROLE_CONSUMER`, `ROLE_BUSINESS`, `ROLE_NGO`, `ROLE_ADMIN`).
- **Database & Persistence:** Relational schema design on **MySQL InnoDB** managed via **Spring Data JPA / Hibernate**, featuring transactional boundaries (`@Transactional`), cascade management, and HikariCP connection pooling.
- **Real-Time Notification Pipeline:** Custom event listener (`TransactionEventListener`) reacting to domain events (`FoodListingCreatedEvent`, `NotificationCreatedEvent`) with **WebSocket STOMP** live broadcasting.
- **Comprehensive REST API:** 15+ controller modules covering food listing catalogs, multi-status order lifecycle, NGO donation claims, reviews/ratings, dispute resolution, and administrative analytics.

👉 **[Explore GitHub Repository →](https://github.com/KshitijShinde26/Surplus_Food_MarketPlace_Project)** &nbsp;|&nbsp; 🌐 **[Live App Preview →](https://surplus-food-market-place-project.vercel.app)**

---

## 💻 Java & Problem Solving

I regularly practice Data Structures and Algorithms using **Java**, focusing on asymptotic efficiency ($O(N)$, $O(\log N)$), object-oriented implementation, and memory optimization.

<div align="center">

[![LeetCode Profile](https://img.shields.io/badge/LeetCode_Profile-@kshitu__26-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/kshitu_26/)
[![LeetCode Solutions Repo](https://img.shields.io/badge/Java_Solutions_Repository-LeetCode-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KshitijShinde26/LeetCode)

</div>

### 📂 Problem Solving Repositories:
- **[LeetCode Solutions (Java)](https://github.com/KshitijShinde26/LeetCode)** — Solutions for coding challenges covering arrays, two pointers, sliding window, binary trees, recursion, and dynamic programming.
- **[Apna College Data Structures](https://github.com/KshitijShinde26/Apna_College_Data_Structure)** — Implementations of stacks, queues, linked lists, binary trees, divide-and-conquer algorithms, and sorting strategies in Java.
- **[College Data Structures](https://github.com/KshitijShinde26/College_Data_Structure)** — Academic data structure assignments, lab implementations, and algorithm problem sets.
- **[Udemy Data Structures in Java](https://github.com/KshitijShinde26/Udemy_Data_Structure_Java)** — Course-driven data structure exercises focusing on linear structures, searching, and sorting algorithms.

---

## 🌐 Other Projects & Supporting Systems

*Client-side and supporting applications built to interact with backend services and demonstrate end-to-end integration:*

- 🧁 **[Payel's Bakery Cottage](https://github.com/KshitijShinde26/Payel-s_Bakery_Cottage)** — Full-stack bakery ecommerce web application built with TypeScript, showcasing product catalogs, cart management, and order flows.
- 💼 **[Portfolio](https://github.com/KshitijShinde26/Portfolio)** — Personal portfolio web presence built with TypeScript and deployed on Vercel.
- 🎮 **[Game](https://github.com/KshitijShinde26/Game)** — Interactive software project built with TypeScript.

---

## 📚 Practice & Learning Repositories

*Foundational repositories documenting structured coursework and core Java practice:*

- **[Full_Stack_Course](https://github.com/KshitijShinde26/Full_Stack_Course)** — Full stack backend modules and service integration exercises in Java.
- **[Java_Course](https://github.com/KshitijShinde26/Java_Course)** — Object-oriented programming principles, interfaces, polymorphism, and collections in Java.
- **[Udemy_Java_Basic](https://github.com/KshitijShinde26/Udemy_Java_Basic)** — Core Java syntax, exception handling, and object modeling practice.

---

## 📊 GitHub Activity & Developer Analytics

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=KshitijShinde26&theme=tokyo-night&hide_border=true&area=true" alt="Dynamic GitHub Contribution Graph" width="98%" />

<br/><br/>

<img src="https://github-readme-stats.vercel.app/api?username=KshitijShinde26&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=false" alt="GitHub Stats" width="48%" />
<img src="https://github-readme-streak-stats.herokuapp.com/?user=KshitijShinde26&theme=tokyonight&hide_border=true" alt="GitHub Streak" width="48%" />

<br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=KshitijShinde26&layout=compact&theme=tokyonight&hide_border=true&langs_count=6" alt="Top Languages" width="52%" />

<p><sub><i>Note: Language distribution reflects client-side UI files in supporting projects; primary backend development is centered on Java.</i></sub></p>

</div>

---

## 🔥 Recent Development

- 🛒 **Surplus Food Marketplace Backend:** Developed REST endpoints for multi-tier food listings, integrated Spring Security 6 stateless JWT filter chain, implemented HikariCP transaction pooling, and configured STOMP WebSockets for live alerts.
- 🧩 **Java Algorithmic Problem Solving:** Maintained daily problem solving in [LeetCode](https://github.com/KshitijShinde26/LeetCode), practicing pattern-based solutions in Java.
- 📚 **Data Structures Implementation:** Structured linear and hierarchical data structure implementations in [Apna_College_Data_Structure](https://github.com/KshitijShinde26/Apna_College_Data_Structure).

---

## 🏆 Education & Certifications

- 🎓 **Bachelor of Engineering — Information Technology (Third Year)**
- 📜 **Java Backend Development Track** — Active engineering in Java core, Spring Boot, JPA/Hibernate, and algorithmic problem solving.

<details>
<summary><b>View Verified Certifications & Coursework</b></summary>
<br/>

*Credentials and verified certifications will be documented here upon completion:*
- 🏅 Core Java & Data Structures Coursework
- 🏅 Spring Boot Backend Architecture & Microservices

</details>

---

## 🤝 Connect With Me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kshitijshinde26/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/kshitu_26/)
[![Email](https://img.shields.io/badge/Email-Get_in_Touch-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kshitij26gs@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit_Website-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://portfolio-delta-six-46.vercel.app)

<br/>

*Open to Java Backend Developer internships, server-side software collaborations, and engineering discussions.*

</div>
