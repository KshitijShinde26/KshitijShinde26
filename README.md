<div align="center">

# ☕ Hi, I'm Kshitij Shinde

### **Java Backend Developer | Third Year IT Engineering Student**
*Engineering robust backend systems, scalable REST APIs, transactional persistence, and secure server-side architectures.*

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kshitijshinde26/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/kshitu_26/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kshitij26gs@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://portfolio-delta-six-46.vercel.app)
[![GitHub Repositories](https://img.shields.io/badge/Public_Repos-11-238636?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KshitijShinde26?tab=repositories)

<br/>

</div>

---

### 📌 Profile Highlights

```ini
[ACADEMIC]      🎓 Third Year B.E. in Information Technology
[CORE FOCUS]    ☕ Java Backend Development & RESTful Microservices
[FLAGSHIP]      🚀 Real-Time Surplus Food Marketplace REST Platform
[ALGORITHMS]    💻 Consistent Problem Solving & Data Structures in Java
[SECURITY]      🔐 Stateless JWT Filter Chains & Role-Based Access Control (RBAC)
[DATABASES]     🗄️ Relational Schema Design, Spring Data JPA & Hibernate ORM
```

---

## ☕ Technical Stack & Core Competencies

<div align="center">

| Domain | Technologies & Frameworks |
| :--- | :--- |
| **Backend Core** | ![Java](https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![Spring MVC](https://img.shields.io/badge/Spring_MVC-6DB33F?style=flat-square&logo=spring&logoColor=white) ![REST APIs](https://img.shields.io/badge/RESTful_APIs-0052CC?style=flat-square&logoColor=white) |
| **Security & Auth** | ![Spring Security](https://img.shields.io/badge/Spring_Security_6-6DB33F?style=flat-square&logo=springsecurity&logoColor=white) ![JWT](https://img.shields.io/badge/JWT_Auth-000000?style=flat-square&logo=jsonwebtokens&logoColor=white) ![RBAC](https://img.shields.io/badge/Role_Based_Access-4B0082?style=flat-square&logoColor=white) |
| **Persistence & DB** | ![Spring Data JPA](https://img.shields.io/badge/Spring_Data_JPA-59666C?style=flat-square&logo=hibernate&logoColor=white) ![Hibernate](https://img.shields.io/badge/Hibernate_ORM-59666C?style=flat-square&logo=hibernate&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL_InnoDB-4479A1?style=flat-square&logo=mysql&logoColor=white) ![HikariCP](https://img.shields.io/badge/HikariCP-003B57?style=flat-square&logoColor=white) |
| **Messaging & Events** | ![WebSockets](https://img.shields.io/badge/WebSockets_STOMP-010101?style=flat-square&logo=socketdotio&logoColor=white) ![Spring Events](https://img.shields.io/badge/ApplicationEventPublisher-6DB33F?style=flat-square&logo=spring&logoColor=white) |
| **Data Validation & Mappings** | ![Jakarta Bean Validation](https://img.shields.io/badge/Jakarta_Validation_JSR--380-107C41?style=flat-square&logoColor=white) ![MapStruct](https://img.shields.io/badge/MapStruct-E58C3A?style=flat-square&logoColor=white) |
| **Build & Tooling** | ![Maven](https://img.shields.io/badge/Apache_Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white) |

</div>

---

## 🚀 Flagship Backend Project

### 🌟 [Surplus Food Marketplace Backend](https://github.com/KshitijShinde26/Surplus_Food_MarketPlace_Project)
> **An enterprise-grade Java REST API platform engineered to connect commercial food businesses (restaurants, supermarkets) with consumers and NGOs for surplus food commerce and donation pipelines.**

```
Client Tier (Web/Mobile UI)
      │
      ▼ (HTTPS / WSS)
[ Spring Security Filter Chain ] ──► Stateless JWT Validation & Security Context
      │
      ▼
[ DispatcherServlet & Spring MVC ] ──► JSR-380 Request Validation & Routing
      │
      ▼
[ Service & Business Logic Tier ] ──► MapStruct DTO Mapping & ApplicationEventPublisher
      │
      ├──► [ Real-Time Notifications ] ──► Spring WebSocket & STOMP Broker
      └──► [ Persistence Layer ] ──► Spring Data JPA / Hibernate (HikariCP)
                 │
                 ▼
          [ MySQL Database ] (ACID Transactions & InnoDB Engine)
```

#### 🔑 Backend Highlights & Architectural Implementation:
- **Modular Architecture:** Built with **Java 21** and **Spring Boot 3.3.5** utilizing clean multi-tiered separation (Controllers, Services, Repositories, DTOs, Mappers).
- **Stateless Security Filter Chain:** Custom `JwtAuthenticationFilter` with token generation, claims verification, refresh token lifecycle, and fine-grained Role-Based Access Control (`ROLE_CONSUMER`, `ROLE_BUSINESS`, `ROLE_NGO`, `ROLE_ADMIN`).
- **Transactional Persistence:** Strict `@Transactional` boundaries with automatic rollback on runtime exceptions, L1/L2 Hibernate caching, and HikariCP connection pooling over a normalized **MySQL InnoDB** schema.
- **Real-Time Notification Pipeline:** Event-driven architecture with `ApplicationEventPublisher` coupled with **WebSocket STOMP endpoints** for real-time order alerts, donation claims, and dispute updates.
- **Robust REST API Surface:** 15+ controller modules covering food cataloging, inventory lifecycle, multi-status ordering, NGO claims, reviews/ratings, image uploads, and transactional analytics.

🔗 **[View GitHub Repository →](https://github.com/KshitijShinde26/Surplus_Food_MarketPlace_Project)** &nbsp;|&nbsp; 🌐 **[Live App Preview →](https://surplus-food-market-place-project.vercel.app)**

---

## 💻 Java & Problem Solving

I regularly practice Data Structures and Algorithms in **Java**, focusing on asymptotic efficiency, clean object-oriented implementations, and memory management.

<div align="center">

[![LeetCode Profile](https://img.shields.io/badge/LeetCode_Profile-@kshitu__26-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/kshitu_26/)
[![LeetCode Java Repo](https://img.shields.io/badge/Java_Solutions_Repository-LeetCode-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KshitijShinde26/LeetCode)

</div>

### 📂 Problem Solving Repositories:
- **[LeetCode Solutions (Java)](https://github.com/KshitijShinde26/LeetCode)** — Curated algorithmic solutions solving array patterns, two pointers, sliding window, binary trees, recursion, and dynamic programming.
- **[Apna College Data Structures](https://github.com/KshitijShinde26/Apna_College_Data_Structure)** — Core implementations of linear and non-linear data structures, recursive divide-and-conquer algorithms, and sorting strategies.
- **[College Data Structures](https://github.com/KshitijShinde26/College_Data_Structure)** — Academic coursework, data structure labs, and algorithm implementations in Java.
- **[Udemy Data Structures in Java](https://github.com/KshitijShinde26/Udemy_Data_Structure_Java)** — Structured exercises focusing on search/sort algorithms and foundational tree operations.

---

## 📂 Public Repositories Directory

### ☕ Java Backend & Core Development
| Repository | Overview | Core Stack |
| :--- | :--- | :--- |
| **[Surplus_Food_MarketPlace_Project](https://github.com/KshitijShinde26/Surplus_Food_MarketPlace_Project)** | Enterprise Surplus Food Marketplace REST Backend | Java 21, Spring Boot 3, Spring Security, JPA, MySQL, WebSockets |
| **[Full_Stack_Course](https://github.com/KshitijShinde26/Full_Stack_Course)** | Backend service modules, API routing, and architectural exercises | Java, Spring Ecosystem |
| **[Java_Course](https://github.com/KshitijShinde26/Java_Course)** | OOP patterns, abstraction, interfaces, polymorphism, and collections | Java SE |
| **[Udemy_Java_Basic](https://github.com/KshitijShinde26/Udemy_Java_Basic)** | Core syntax, class design, exception handling, and standard I/O | Java SE |

### 🧠 Data Structures & Algorithms
| Repository | Focus Areas | Language |
| :--- | :--- | :--- |
| **[LeetCode](https://github.com/KshitijShinde26/LeetCode)** | Algorithmic problem solving across data structures & DP | Java |
| **[Apna_College_Data_Structure](https://github.com/KshitijShinde26/Apna_College_Data_Structure)** | Stacks, Queues, Linked Lists, Trees, Graph traversals | Java |
| **[College_Data_Structure](https://github.com/KshitijShinde26/College_Data_Structure)** | Core curriculum algorithms, searching, sorting routines | Java |
| **[Udemy_Data_Structure_Java](https://github.com/KshitijShinde26/Udemy_Data_Structure_Java)** | Algorithmic fundamentals and practical data structures | Java |

### 🌐 Supporting Web Projects
*Client-side and supporting applications built to consume REST services and showcase end-to-end integration:*
- **[Payel-s_Bakery_Cottage](https://github.com/KshitijShinde26/Payel-s_Bakery_Cottage)** — Bakery ecommerce web application.
- **[Portfolio](https://github.com/KshitijShinde26/Portfolio)** — Personal portfolio web presence showcasing developer profile.
- **[Game](https://github.com/KshitijShinde26/Game)** — Interactive software build.

---

## 🗂️ Engineering Timeline

```text
2025
 ├── Core Java Fundamentals & OOP (`Java_Course`, `Udemy_Java_Basic`)
 └── Foundational Data Structures & Algorithms (`College_Data_Structure`, `Udemy_Data_Structure_Java`)
│
2026
 ├── Advanced DSA Implementation & LeetCode Practice (`Apna_College_Data_Structure`, `LeetCode`)
 ├── Full-Stack Integration & Client Systems (`Payel-s_Bakery_Cottage`, `Portfolio`)
 └── Enterprise Backend Engineering with Java 21 & Spring Boot 3 (`Surplus_Food_MarketPlace_Project`)
```

---

## 🏆 Education & Certifications

- 🎓 **Bachelor of Engineering — Information Technology (Third Year)**
- 📜 **Java & Backend Development Track** — Continuous engineering in Java core, Spring Boot, and algorithmic problem solving.

<!-- Expandable section for verified certifications -->
<details>
<summary><b>View Verified Certifications & Coursework</b></summary>
<br/>

*Certifications and credentials will be updated as completed:*
- 🏅 Core Java & Data Structures Program
- 🏅 Enterprise Backend Development with Spring Boot

</details>

---

## 📊 GitHub Analytics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=KshitijShinde26&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=false" alt="GitHub Stats" width="48%" />
<img src="https://github-readme-streak-stats.herokuapp.com/?user=KshitijShinde26&theme=tokyonight&hide_border=true" alt="GitHub Streak" width="48%" />

<br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=KshitijShinde26&layout=compact&theme=tokyonight&hide_border=true&langs_count=6" alt="Top Languages" width="52%" />

</div>

---

## 🤝 Connect With Me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kshitijshinde26/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/kshitu_26/)
[![Email](https://img.shields.io/badge/Email-Get_in_Touch-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kshitij26gs@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit_Website-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://portfolio-delta-six-46.vercel.app)

<br/>

*Open to Java Backend Developer internships, backend engineering collaborations, and server-side software discussions.*

</div>
