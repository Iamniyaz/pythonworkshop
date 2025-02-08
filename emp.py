import module as em

em.college()
print(em.location)
emp = em.Employee("zafar","Associate Professor")
emp.show()

from module import*
em.college()
print(em.location)

