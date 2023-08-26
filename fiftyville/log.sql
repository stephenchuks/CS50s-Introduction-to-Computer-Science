fiftyville/ $ sqlite3 fiftyville.db
sqlite> -- Crime Scene Reports Query
sqlite> SELECT *
   ...> FROM crime_scene_reports
   ...> WHERE month = 7 AND day = 28
   ...> AND street = 'Humphrey Street';
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  | year | month | day |     street      |                                                                                                       description                                                                                                        |
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 295 | 2021 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
| 297 | 2021 | 7     | 28  | Humphrey Street | Littering took place at 16:36. No known witnesses.                                                                                                                                                                       |
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
sqlite>
sqlite> SELECT *
   ...> FROM interviews
   ...> WHERE month = 7 AND day = 28;
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  |  name   | year | month | day |                                                                                                                                                     transcript                                                                                                                                                      |
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 158 | Jose    | 2021 | 7     | 28  | “Ah,” said he, “I forgot that I had not seen you for some weeks. It is a little souvenir from the King of Bohemia in return for my assistance in the case of the Irene Adler papers.”                                                                                                                               |
| 159 | Eugene  | 2021 | 7     | 28  | “I suppose,” said Holmes, “that when Mr. Windibank came back from France he was very annoyed at your having gone to the ball.”                                                                                                                                                                                      |
| 160 | Barbara | 2021 | 7     | 28  | “You had my note?” he asked with a deep harsh voice and a strongly marked German accent. “I told you that I would call.” He looked from one to the other of us, as if uncertain which to address.                                                                                                                   |
| 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
| 191 | Lily    | 2021 | 7     | 28  | Our neighboring courthouse has a very annoying rooster that crows loudly at 6am every day. My sons Robert and Patrick took the rooster to a city far, far away, so it may never bother us again. My sons have successfully arrived in Paris.                                                                        |
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
sqlite>
sqlite> SELECT a.city
   ...> FROM airports a
   ...> JOIN flights f ON a.id = f.destination_airport_id
   ...> WHERE f.month = 7 AND f.day = 29
   ...> AND a.city = 'Fiftyville'
   ...> ORDER BY f.hour, f.minute
   ...> LIMIT 1;
sqlite>
sqlite> SELECT p.id, p.name, p.phone_number, p.passport_number, p.license_plate
   ...> FROM people p
   ...> JOIN bank_accounts ba ON p.id = ba.person_id
   ...> JOIN atm_transactions atm ON ba.account_number = atm.account_number
   ...> JOIN bakery_security_logs bsl ON p.license_plate = bsl.license_plate
   ...> JOIN phone_calls pc ON p.phone_number = pc.caller
   ...> JOIN passengers ps ON p.passport_number = ps.passport_number
   ...> JOIN flights f ON ps.flight_id = f.id
   ...> WHERE atm.month = 7 AND atm.day = 28
   ...> AND atm.atm_location = 'Leggett Street'
   ...> AND atm.transaction_type = 'withdraw'
   ...> AND bsl.month = 7 AND bsl.day = 28
   ...> AND bsl.hour = 10
   ...> AND bsl.minute BETWEEN 15 AND 25
   ...> AND pc.month = 7 AND pc.day = 28
   ...> AND pc.duration < 60
   ...> AND f.origin_airport_id = (
   ...>     SELECT id
   ...>     FROM airports
   ...>     WHERE city = 'Fiftyville'
   ...>     LIMIT 1
   ...> )
   ...> AND f.month = 7 AND f.day = 29
   ...> ORDER BY f.hour, f.minute
   ...> LIMIT 1;
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+-------+----------------+-----------------+---------------+
sqlite>
sqlite>
sqlite> -- Accomplice Query
sqlite> SELECT p.id, p.name, p.phone_number, p.passport_number, p.license_plate
   ...> FROM people p
   ...> JOIN phone_calls pc ON p.phone_number = pc.receiver
   ...> WHERE pc.month = 7 AND pc.day = 28
   ...> AND pc.duration < 60
   ...> AND pc.caller = '(367) 555-5533';
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
+--------+-------+----------------+-----------------+---------------+
sqlite>