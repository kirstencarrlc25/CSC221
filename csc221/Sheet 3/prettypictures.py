from gasp import *
begin_graphics()
for r in 100, 110, 120, 130, 140:
    Circle((300, 200), 100)#head
    Arc((300, 200), 50, 225, 315)#smile
    Circle((260, 230), 20)#left eye
    Circle((338, 230), 20)#right eye
    Circle((340, 232), 5.5)#left pulip
    Circle((262, 232), 5.5)#right pupil

update_when('key_pressed')
end_graphics 