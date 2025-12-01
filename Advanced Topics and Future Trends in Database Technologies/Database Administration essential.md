*Topic:* Concurrency, Logs, and Recovery

## 1. Transaction Logs
* *What they are:* A sequential record of all changes made to the database.
* *Key takeaway:* Transaction logs are the first line of defense. Before data is written to the actual table file, it is written to the log (Write-Ahead Logging). This ensures that if the system crashes, the database can "replay" the log to restore the state.

## 2. Database Backup & Recovery
* *Recovery Models:* Learned about how different recovery models (Simple vs. Full) impact how logs are managed.
* *Importance:* A backup strategy isn't just about saving data; it's about RPO (Recovery Point Objective) and RTO (Recovery Time Objective)—how much data can we afford to lose, and how fast can we get it back?

## 3. Database Concurrency
* *The Challenge:* Managing multiple users accessing the same data simultaneously without corrupting it.
* *The Solution:* Locking mechanisms and Isolation levels (ACID properties).
* *Insight:* High concurrency requires careful management of locks to avoid "deadlocks" where two processes wait for each other forever.

## 4. Career Path in DB Tech
* Exploring roles like Database Administrator (DBA), Data Engineer, and Backend Engineer.
* Focusing on mastering the fundamentals of storage engines and query optimization.
*
