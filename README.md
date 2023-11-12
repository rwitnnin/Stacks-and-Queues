# Stacks-and-Queues
![Screenshot 2023-11-12 230135](https://github.com/rwitnnin/Stacks-and-Queues/assets/150579607/80a16e47-5155-42a9-832a-5890c7dff23b)
คลาส Stack
นี่เป็นการเขียนโค้ดเพื่อสร้างโครงสร้างข้อมูลแบบสแต็ค (stack) ที่เป็นการรวบรวมข้อมูลซึ่งสนับสนุนการเพิ่มและลบข้อมูลแบบหลังเข้าก่อนออก (LIFO)

__init__: เริ่มต้นด้วยการสร้างลิสต์ว่างเพื่อเก็บข้อมูลของสแต็ค
isEmpty: คืนค่า True ถ้าสแต็คว่าง, False ถ้าไม่ว่าง
push: เพิ่มข้อมูลไปที่ยอดของสแต็ค
pop: ลบและคืนค่าข้อมูลจากยอดของสแต็ค
peek: คืนค่าข้อมูลที่ยอดของสแต็คโดยไม่ลบออก
size: คืนค่าจำนวนข้อมูลในสแต็ค

ฟังก์ชัน bracket_check
ฟังก์ชันนี้ใช้เพื่อตรวจสอบว่าสตริงมีเครื่องหมายวงเล็บที่สมดุลกันหรือไม่ โดยใช้ Stack เพื่อตรวจสอบว่าทุกวงเล็บเปิดมีวงเล็บปิดที่ตรงกันในลำดับที่ถูกต้อง

ฟังก์ชันจะวนลูปผ่านทุกตัวอักษรในสตริง
ถ้าพบวงเล็บเปิด ((, [, {) จะทำการเพิ่มลงในสแต็ค
ถ้าพบวงเล็บปิด (), ], }) จะทำการนำวงเล็บออกจากสแต็คและตรวจสอบว่าตรงกับวงเล็บเปิดที่ถูกนำออกหรือไม่ ถ้าไม่ตรงกันหรือสแต็คว่างอยู่ จะถือเป็นข้อผิดพลาดและบันทึกตำแหน่งของตัวอักษรนั้น
หลังจากวนลูปเสร็จ ถ้าสแต็คไม่ว่าง (คือมีวงเล็บเปิดที่ไม่มีคู่) จะถือว่าเป็นข้อผิดพลาด

Unit Tests
ในสคริปต์มีการเขียน unit tests โดยใช้เฟรมเวิร์ก unittest ของ Python เพื่อทดสอบความถูกต้องของฟังก์ชัน bracket_check

test_no_error: ตรวจสอบว่าฟังก์ชันสามารถระบุสตริงที่ไม่มีข้อผิดพลาดในเรื่องวงเล็บได้อย่างถูกต้อง
test_error_1 ถึง test_error_4: การทดสอบเหล่านี้ตรวจสอบสถานการณ์ต่างๆที่ควรจะตรวจพบข้อผิดพลาดเกี่ยวกับวงเล็บ เช่น วงเล็บที่ไม่มีคู่หรือการซ้อนทับที่ไม่ถูกต้อง
