from miniproject import Chatbook

cb = Chatbook()
print(cb.get_id())

Chatbook.set_id(10)

print(cb.get_id())


cb1 = Chatbook()
print(cb1.get_id())

Chatbook.set_id(102)

print(cb.get_id())