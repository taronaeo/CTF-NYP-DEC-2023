import random
'''
*WARNING* 
UNCALIBRATED CATCHING ALGORITHM 
USE WITH CAUTION!!
*WARNING*

*Cypher note*
Try to observe patterns, they may mean something. Find the information that is
missing.
'''
def return_b(a):
   if a == 0:
       b = chr(97)
   if a == 1:
       b = chr(119)
   if a == 2:
       b = chr(112)
   if a == 3:
       b = chr(83)
   if a == 4:
       b = chr(14)
   if a == 5:
       b = chr(113)
   if a == 6:
       b = chr(32)
   if a == 7:
       b = chr(26)
   if a == 8:
       b = chr(60)
   if a == 9:
       b = chr(109)
   if a == 10:
       b = chr(77)
   if a == 11:
       b = chr(47)
   if a == 12:
       b = chr(81)
   if a == 13:
       b = chr(45)
   if a == 14:
       b = chr(1)
   if a == 15:
       b = chr(2)
   if a == 16:
       b = chr(50)
   if a == 17:
       b = chr(9)
   if a == 18:
       b = chr(96)
   if a == 19:
       b = chr(13)
   if a == 20:
       b = chr(42)
   if a == 21:
       b = chr(58)
   if a == 22:
       b = chr(66)
   if a == 23:
       b = chr(99)
   if a == 24:
       b = chr(67)
   if a == 25:
       b = chr(18)
   if a == 26:
       b = chr(29)
   if a == 27:
       b = chr(114)
   if a == 28:
       b = chr(70)
   if a == 29:
       b = chr(94)
   if a == 30:
       b = chr(44)
   if a == 31:
       b = chr(53)
   if a == 32:
       b = chr(127)
   if a == 33:
       b = chr(40)
   if a == 34:
       b = chr(69)
   if a == 35:
       b = chr(7)
   if a == 36:
       b = chr(68)
   if a == 37:
       b = chr(79)
   if a == 38:
       b = chr(106)
   if a == 39:
       b = chr(41)
   if a == 40:
       b = chr(61)
   if a == 41:
       b = chr(28)
   if a == 42:
       b = chr(62)
   if a == 43:
       b = chr(25)
   if a == 44:
       b = chr(27)
   if a == 45:
       b = chr(35)
   if a == 46:
       b = chr(34)
   if a == 47:
       b = chr(122)
   if a == 48:
       b = chr(110)
   if a == 49:
       b = chr(19)
   if a == 50:
       b = chr(84)
   if a == 51:
       b = chr(75)
   if a == 52:
       b = chr(100)
   if a == 53:
       b = chr(39)
   if a == 54:
       b = chr(4)
   if a == 55:
       b = chr(101)
   if a == 56:
       b = chr(104)
   if a == 57:
       b = chr(37)
   if a == 58:
       b = chr(48)
   if a == 59:
       b = chr(6)
   if a == 60:
       b = chr(125)
   if a == 61:
       b = chr(0)
   if a == 62:
       b = chr(90)
   if a == 63:
       b = chr(64)
   if a == 64:
       b = chr(51)
   if a == 65:
       b = chr(20)
   if a == 66:
       b = chr(82)
   if a == 67:
       b = chr(5)
   if a == 68:
       b = chr(36)
   if a == 69:
       b = chr(105)
   if a == 70:
       b = chr(102)
   if a == 71:
       b = chr(73)
   if a == 72:
       b = chr(56)
   if a == 73:
       b = chr(120)
   if a == 74:
       b = chr(117)
   if a == 75:
       b = chr(111)
   if a == 76:
       b = chr(76)
   if a == 77:
       b = chr(3)
   if a == 78:
       b = chr(63)
   if a == 79:
       b = chr(108)
   if a == 80:
       b = chr(118)
   if a == 81:
       b = chr(57)
   if a == 82:
       b = chr(30)
   if a == 83:
       b = chr(87)
   if a == 84:
       b = chr(24)
   if a == 85:
       b = chr(10)
   if a == 86:
       b = chr(80)
   if a == 87:
       b = chr(17)
   if a == 88:
       b = chr(23)
   if a == 89:
       b = chr(72)
   if a == 90:
       b = chr(21)
   if a == 91:
       b = chr(59)
   if a == 92:
       b = chr(33)
   if a == 93:
       b = chr(8)
   if a == 94:
       b = chr(49)
   if a == 95:
       b = chr(11)
   if a == 96:
       b = chr(12)
   if a == 97:
       b = chr(115)
   if a == 98:
       b = chr(22)
   if a == 99:
       b = chr(93)
   if a == 100:
       b = chr(95)
   if a == 101:
       b = chr(123)
   if a == 102:
       b = chr(85)
   if a == 103:
       b = chr(65)
   if a == 104:
       b = chr(74)
   if a == 105:
       b = chr(43)
   if a == 106:
       b = chr(71)
   if a == 107:
       b = chr(52)
   if a == 108:
       b = chr(15)
   if a == 109:
       b = chr(16)
   if a == 110:
       b = chr(89)
   if a == 111:
       b = chr(31)
   if a == 112:
       b = chr(54)
   if a == 113:
       b = chr(92)
   if a == 114:
       b = chr(126)
   if a == 115:
       b = chr(78) 
   if a == 116:
       b = chr(98)
   if a == 117:
       b = chr(38)
   if a == 118:
       b = chr(46)
   if a == 119:
       b = chr(55)
   if a == 120:
       b = chr(91)
   if a == 121:
       b = chr(88)
   if a == 122:
       b = chr(103)
   if a == 123:
       b = chr(116)
   if a == 124:
       b = chr(121)
   if a == 125:
       b = chr(124)
   if a == 126:
       b = chr(86)
   return b

def return_d(c):
   if c == 0:
       d = chr(18)
   if c == 1:
       d = chr(74)
   if c == 2:
       d = chr(127)
   if c == 3:
       d = chr(106)
   if c == 4:
       d = chr(56)
   if c == 5:
       d = chr(98)
   if c == 6:
       d = chr(29)
   if c == 7:
       d = chr(72)
   if c == 8:
       d = chr(82)
   if c == 9:
       d = chr(53)
   if c == 10:
       d = chr(59)
   if c == 11:
       d = chr(86)
   if c == 12:
       d = chr(32)
   if c == 13:
       d = chr(9)
   if c == 14:
       d = chr(123)
   if c == 15:
       d = chr(31)
   if c == 16:
       d = chr(101)
   if c == 17:
       d = chr(104)
   if c == 18:
       d = chr(115)
   if c == 19:
       d = chr(14)
   if c == 20:
       d = chr(125)
   if c == 21:
       d = chr(71)
   if c == 22:
       d = chr(57)
   if c == 23:
       d = chr(64)
   if c == 24:
       d = chr(111)
   if c == 25:
       d = chr(67)
   if c == 26:
       d = chr(84)
   if c == 27:
       d = chr(23)
   if c == 28:
       d = chr(4)
   if c == 29:
       d = chr(40)
   if c == 30:
       d = chr(91)
   if c == 31:
       d = chr(126)
   if c == 32:
       d = chr(94)
   if c == 33:
       d = chr(102)
   if c == 34:
       d = chr(8)
   if c == 35:
       d = chr(51)
   if c == 36:
       d = chr(61)
   if c == 37:
       d = chr(25)
   if c == 38:
       d = chr(99)
   if c == 39:
       d = chr(116)
   if c == 40:
       d = chr(109)
   if c == 41:
       d = chr(48)
   if c == 42:
       d = chr(54)
   if c == 43:
       d = chr(83)
   if c == 44:
       d = chr(122)
   if c == 45:
       d = chr(50)
   if c == 46:
       d = chr(105)
   if c == 47:
       d = chr(39)
   if c == 48:
       d = chr(81)
   if c == 49:
       d = chr(2)
   if c == 50:
       d = chr(70)
   if c == 51:
       d = chr(44)
   if c == 52:
       d = chr(96)
   if c == 53:
       d = chr(73)
   if c == 54:
       d = chr(41)
   if c == 55:
       d = chr(90)
   if c == 56:
       d = chr(117)
   if c == 57:
       d = chr(26)
   if c == 58:
       d = chr(22)
   if c == 59:
       d = chr(36)
   if c == 60:
       d = chr(33)
   if c == 61:
       d = chr(58)
   if c == 62:
       d = chr(7)
   if c == 63:
       d = chr(114)
   if c == 64:
       d = chr(69)
   if c == 65:
       d = chr(121)
   if c == 66:
       d = chr(16)
   if c == 67:
       d = chr(66)
   if c == 68:
       d = chr(46)
   if c == 69:
       d = chr(93)
   if c == 70:
       d = chr(52)
   if c == 71:
       d = chr(24)
   if c == 72:
       d = chr(10)
   if c == 73:
       d = chr(42)
   if c == 74:
       d = chr(97)
   if c == 75:
       d = chr(0)
   if c == 76:
       d = chr(1)
   if c == 77:
       d = chr(68)
   if c == 78:
       d = chr(38)
   if c == 79:
       d = chr(12)
   if c == 80:
       d = chr(103)
   if c == 81:
       d = chr(6)
   if c == 82:
       d = chr(11)
   if c == 83:
       d = chr(79)
   if c == 84:
       d = chr(108)
   if c == 85:
       d = chr(28)
   if c == 86:
       d = chr(35)
   if c == 87:
       d = chr(63)
   if c == 88:
       d = chr(37)
   if c == 89:
       d = chr(92)
   if c == 90:
       d = chr(15)
   if c == 91:
       d = chr(47)
   if c == 92:
       d = chr(65)
   if c == 93:
       d = chr(107)
   if c == 94:
       d = chr(19)
   if c == 95:
       d = chr(88)
   if c == 96:
       d = chr(89) 
   if c == 97:
       d = chr(119)
   if c == 98:
       d = chr(55)
   if c == 99:
       d = chr(30)
   if c == 100:
       d = chr(85)
   if c == 101:
       d = chr(21)
   if c == 102:
       d = chr(45)
   if c == 103:
       d = chr(49)
   if c == 104:
       d = chr(100)
   if c == 105:
       d = chr(3)
   if c == 106:
       d = chr(43)
   if c == 107:
       d = chr(112)
   if c == 108:
       d = chr(62)
   if c == 109:
       d = chr(110)
   if c == 110:
       d = chr(124)
   if c == 111:
       d = chr(95)
   if c == 112:
       d = chr(113)
   if c == 113:
       d = chr(87)
   if c == 114:
       d = chr(20)
   if c == 115:
       d = chr(60)
   if c == 116:
       d = chr(75)
   if c == 117:
       d = chr(77)
   if c == 118:
       d = chr(118)
   if c == 119:
       d = chr(27)
   if c == 120:
       d = chr(76)
   if c == 121:
       d = chr(17)
   if c == 122:
       d = chr(120)
   if c == 123:
       d = chr(13)
   if c == 124:
       d = chr(5)
   if c == 125:
       d = chr(34)
   if c == 126:
       d = chr(80) 
   return d

def return_f(e):
   if e == 0:
       f = chr(21)
   if e == 1:
       f = chr(57)
   if e == 2:
       f = chr(55)
   if e == 3:
       f = chr(30)
   if e == 4:
       f = chr(35)
   if e == 5:
       f = chr(121)
   if e == 6:
       f = chr(86)
   if e == 7:
       f = chr(79)
   if e == 8:
       f = chr(23)
   if e == 9:
       f = chr(101)
   if e == 10:
       f = chr(112)
   if e == 11:
       f = chr(2)
   if e == 12:
       f = chr(98)
   if e == 13:
       f = chr(41)
   if e == 14:
       f = chr(61)
   if e == 15:
       f = chr(120)
   if e == 16:
       f = chr(82)
   if e == 17:
       f = chr(24)
   if e == 18:
       f = chr(119)
   if e == 19:
       f = chr(53)
   if e == 20:
       f = chr(14)
   if e == 21:
       f = chr(83)
   if e == 22:
       f = chr(66)
   if e == 23:
       f = chr(65)
   if e == 24:
       f = chr(22)
   if e == 25:
       f = chr(63)
   if e == 26:
       f = chr(3)
   if e == 27:
       f = chr(27)
   if e == 28:
       f = chr(73)
   if e == 29:
       f = chr(110)
   if e == 30:
       f = chr(45)
   if e == 31:
       f = chr(37)
   if e == 32:
       f = chr(34)
   if e == 33:
       f = chr(8)
   if e == 34:
       f = chr(80) 
   if e == 35:
       f = chr(36)
   if e == 36:
       f = chr(70)
   if e == 37:
       f = chr(123)
   if e == 38:
       f = chr(104)
   if e == 39:
       f = chr(126)
   if e == 40:
       f = chr(18)
   if e == 41:
       f = chr(94)
   if e == 42:
       f = chr(105)
   if e == 43:
       f = chr(10)
   if e == 44:
       f = chr(43)
   if e == 45:
       f = chr(75)
   if e == 46:
       f = chr(26)
   if e == 47:
       f = chr(5)
   if e == 48:
       f = chr(7)
   if e == 49:
       f = chr(17)
   if e == 50:
       f = chr(67)
   if e == 51:
       f = chr(20)
   if e == 52:
       f = chr(77)
   if e == 53:
       f = chr(13)
   if e == 54:
       f = chr(44)
   if e == 55:
       f = chr(108)
   if e == 56:
       f = chr(76)
   if e == 57:
       f = chr(59)
   if e == 58:
       f = chr(106)
   if e == 59:
       f = chr(91)
   if e == 60:
       f = chr(116)
   if e == 61:
       f = chr(48)
   if e == 62:
       f = chr(117)
   if e == 63:
       f = chr(74)
   if e == 64:
       f = chr(38)
   if e == 65:
       f = chr(88)
   if e == 66:
       f = chr(49)
   if e == 67:
       f = chr(25)
   if e == 68:
       f = chr(4)
   if e == 69:
       f = chr(58)
   if e == 70:
       f = chr(93)
   if e == 71:
       f = chr(84)
   if e == 72:
       f = chr(125)
   if e == 73:
       f = chr(54)
   if e == 74:
       f = chr(103)
   if e == 75:
       f = chr(62)
   if e == 76:
       f = chr(15)
   if e == 77:
       f = chr(100)
   if e == 78:
       f = chr(109)
   if e == 79:
       f = chr(68)
   if e == 80:
       f = chr(124)
   if e == 81:
       f = chr(28)
   if e == 82:
       f = chr(31)
   if e == 83:
       f = chr(12)
   if e == 84:
       f = chr(51)
   if e == 85:
       f = chr(113)
   if e == 86:
       f = chr(107)
   if e == 87:
       f = chr(39)
   if e == 88:
       f = chr(90)
   if e == 89:
       f = chr(9)
   if e == 90:
       f = chr(118)
   if e == 91:
       f = chr(127)
   if e == 92:
       f = chr(81)
   if e == 93:
       f = chr(11)
   if e == 94:
       f = chr(64)
   if e == 95:
       f = chr(16)
   if e == 96:
       f = chr(115)
   if e == 97:
       f = chr(56)
   if e == 98:
       f = chr(69)
   if e == 99:
       f = chr(42)
   if e == 100:
       f = chr(52)
   if e == 101:
       f = chr(19)
   if e == 102:
       f = chr(97)
   if e == 103:
       f = chr(1)
   if e == 104:
       f = chr(0)
   if e == 105:
       f = chr(72)
   if e == 106:
       f = chr(50)
   if e == 107:
       f = chr(46)
   if e == 108:
       f = chr(85)
   if e == 109:
       f = chr(47)
   if e == 110:
       f = chr(111)
   if e == 111:
       f = chr(60)
   if e == 112:
       f = chr(92)
   if e == 113:
       f = chr(33)
   if e == 114:
       f = chr(6)
   if e == 115:
       f = chr(96)
   if e == 116:
       f = chr(102)
   if e == 117:
       f = chr(71)
   if e == 118:
       f = chr(78)
   if e == 119:
       f = chr(32)
   if e == 120:
       f = chr(95)
   if e == 121:
       f = chr(122)
   if e == 122:
       f = chr(114)
   if e == 123:
       f = chr(87)
   if e == 124:
       f = chr(99)
   if e == 125:
       f = chr(29)
   if e == 126:
       f = chr(40)
   return f

def return_h(g):
   if g == 0:
       h = chr(66)
   if g == 1:
       h = chr(5)
   if g == 2:
       h = chr(103)
   if g == 3:
       h = chr(51)
   if g == 4:
       h = chr(84)
   if g == 5:
       h = chr(78)
   if g == 6:
       h = chr(20)
   if g == 7:
       h = chr(116)
   if g == 8:
       h = chr(118)
   if g == 9:
       h = chr(52)
   if g == 10:
       h = chr(55)
   if g == 11:
       h = chr(96)
   if g == 12:
       h = chr(35)
   if g == 13:
       h = chr(82)
   if g == 14:
       h = chr(45)
   if g == 15:
       h = chr(76)
   if g == 16:
       h = chr(23)
   if g == 17:
       h = chr(53)
   if g == 18:
       h = chr(7)
   if g == 19:
       h = chr(94)
   if g == 20:
       h = chr(68)
   if g == 21:
       h = chr(73)
   if g == 22:
       h = chr(89)
   if g == 23:
       h = chr(26)
   if g == 24:
       h = chr(77)
   if g == 25:
       h = chr(95)
   if g == 26:
       h = chr(24)
   if g == 27:
       h = chr(43)
   if g == 28:
       h = chr(67)
   if g == 29:
       h = chr(90)
   if g == 30:
       h = chr(61)
   if g == 31:
       h = chr(21)
   if g == 32:
       h = chr(38)
   if g == 33:
       h = chr(97)
   if g == 34:
       h = chr(50)
   if g == 35:
       h = chr(42)
   if g == 36:
       h = chr(93)
   if g == 37:
       h = chr(117)
   if g == 38:
       h = chr(123) 
   if g == 39:
       h = chr(71)
   if g == 40:
       h = chr(70)
   if g == 41:
       h = chr(49)
   if g == 42:
       h = chr(34)
   if g == 43:
       h = chr(11)
   if g == 44:
       h = chr(63)
   if g == 45:
       h = chr(102)
   if g == 46:
       h = chr(109)
   if g == 47:
       h = chr(104)
   if g == 48:
       h = chr(126)
   if g == 49:
       h = chr(99)
   if g == 50:
       h = chr(120)
   if g == 51:
       h = chr(112)
   if g == 52:
       h = chr(39)
   if g == 53:
       h = chr(100)
   if g == 54:
       h = chr(41)
   if g == 55:
       h = chr(40)
   if g == 56:
       h = chr(64)
   if g == 57:
       h = chr(79)
   if g == 58:
       h = chr(125)
   if g == 59:
       h = chr(75)
   if g == 60:
       h = chr(60)
   if g == 61:
       h = chr(44)
   if g == 62:
       h = chr(46)
   if g == 63:
       h = chr(14)
   if g == 64:
       h = chr(92)
   if g == 65:
       h = chr(105)
   if g == 66:
       h = chr(29)
   if g == 67:
       h = chr(108)
   if g == 68:
       h = chr(98)
   if g == 69:
       h = chr(91)
   if g == 70:
       h = chr(81)
   if g == 71:
       h = chr(62)
   if g == 72:
       h = chr(9)
   if g == 73:
       h = chr(119)
   if g == 74:
       h = chr(17)
   if g == 75:
       h = chr(121)
   if g == 76:
       h = chr(101)
   if g == 77:
       h = chr(1)
   if g == 78:
       h = chr(28)
   if g == 79:
       h = chr(2)
   if g == 80:
       h = chr(69)
   if g == 81:
       h = chr(27)
   if g == 82:
       h = chr(12)
   if g == 83:
       h = chr(57)
   if g == 84:
       h = chr(124)
   if g == 85:
       h = chr(19)
   if g == 86:
       h = chr(13)
   if g == 87:
       h = chr(10)
   if g == 88:
       h = chr(36)
   if g == 89:
       h = chr(25)
   if g == 90:
       h = chr(85)
   if g == 91:
       h = chr(30)
   if g == 92:
       h = chr(6)
   if g == 93:
       h = chr(127)
   if g == 94:
       h = chr(59)
   if g == 95:
       h = chr(72)
   if g == 96:
       h = chr(65)
   if g == 97:
       h = chr(115)
   if g == 98:
       h = chr(31)
   if g == 99:
       h = chr(16)
   if g == 100:
       h = chr(110)
   if g == 101:
       h = chr(56)
   if g == 102:
       h = chr(18)
   if g == 103:
       h = chr(3)
   if g == 104:
       h = chr(0)
   if g == 105:
       h = chr(122)
   if g == 106:
       h = chr(107)
   if g == 107:
       h = chr(4)
   if g == 108:
       h = chr(15)
   if g == 109:
       h = chr(74)
   if g == 110:
       h = chr(111)
   if g == 111:
       h = chr(106)
   if g == 112:
       h = chr(32)
   if g == 113:
       h = chr(83)
   if g == 114:
       h = chr(86)
   if g == 115:
       h = chr(48)
   if g == 116:
       h = chr(33)
   if g == 117:
       h = chr(8)
   if g == 118:
       h = chr(113)
   if g == 119:
       h = chr(22)
   if g == 120:
       h = chr(37)
   if g == 121:
       h = chr(47)
   if g == 122:
       h = chr(54)
   if g == 123:
       h = chr(114)
   if g == 124:
       h = chr(58)
   if g == 125:
       h = chr(88)
   if g == 126:
       h = chr(87)
   return h

def return_k(i):
   if i == 0:
       k = chr(38)
   if i == 1:
       k = chr(30)
   if i == 2:
       k = chr(18)
   if i == 3:
       k = chr(79)
   if i == 4:
       k = chr(108)
   if i == 5:
       k = chr(41)
   if i == 6:
       k = chr(59)
   if i == 7:
       k = chr(46)
   if i == 8:
       k = chr(11)
   if i == 9:
       k = chr(12)
   if i == 10:
       k = chr(63)
   if i == 11:
       k = chr(100)
   if i == 12:
       k = chr(82)
   if i == 13:
       k = chr(28)
   if i == 14:
       k = chr(7)
   if i == 15:
       k = chr(111)
   if i == 16:
       k = chr(5)
   if i == 17:
       k = chr(80)
   if i == 18:
       k = chr(70)
   if i == 19:
       k = chr(14)
   if i == 20:
       k = chr(15)
   if i == 21:
       k = chr(94)
   if i == 22:
       k = chr(35)
   if i == 23:
       k = chr(91)
   if i == 24:
       k = chr(93)
   if i == 25:
       k = chr(44)
   if i == 26:
       k = chr(106)
   if i == 27:
       k = chr(31)
   if i == 28:
       k = chr(121)
   if i == 29:
       k = chr(92)
   if i == 30:
       k = chr(78)
   if i == 31:
       k = chr(34)
   if i == 32:
       k = chr(65)
   if i == 33:
       k = chr(73)
   if i == 34:
       k = chr(55)
   if i == 35:
       k = chr(8)
   if i == 36:
       k = chr(39)
   if i == 37:
       k = chr(99) 
   if i == 38:
       k = chr(6)
   if i == 39:
       k = chr(74)
   if i == 40:
       k = chr(114)
   if i == 41:
       k = chr(113)
   if i == 42:
       k = chr(124)
   if i == 43:
       k = chr(76)
   if i == 44:
       k = chr(110)
   if i == 45:
       k = chr(22)
   if i == 46:
       k = chr(85)
   if i == 47:
       k = chr(33)
   if i == 48:
       k = chr(71)
   if i == 49:
       k = chr(58)
   if i == 50:
       k = chr(126)
   if i == 51:
       k = chr(9)
   if i == 52:
       k = chr(43)
   if i == 53:
       k = chr(68)
   if i == 54:
       k = chr(21)
   if i == 55:
       k = chr(29)
   if i == 56:
       k = chr(24)
   if i == 57:
       k = chr(88)
   if i == 58:
       k = chr(112)
   if i == 59:
       k = chr(102)
   if i == 60:
       k = chr(50)
   if i == 61:
       k = chr(104)
   if i == 62:
       k = chr(48)
   if i == 63:
       k = chr(17)
   if i == 64:
       k = chr(98)
   if i == 65:
       k = chr(26)
   if i == 66:
       k = chr(64)
   if i == 67:
       k = chr(57)
   if i == 68:
       k = chr(25)
   if i == 69:
       k = chr(53)
   if i == 70:
       k = chr(42)
   if i == 71:
       k = chr(32)
   if i == 72:
       k = chr(96)
   if i == 73:
       k = chr(36)
   if i == 74:
       k = chr(52)
   if i == 75:
       k = chr(69)
   if i == 76:
       k = chr(27)
   if i == 77:
       k = chr(54)
   if i == 78:
       k = chr(13)
   if i == 79:
       k = chr(84)
   if i == 80:
       k = chr(60)
   if i == 81:
       k = chr(0)
   if i == 82:
       k = chr(56)
   if i == 83:
       k = chr(19)
   if i == 84:
       k = chr(97)
   if i == 85:
       k = chr(72)
   if i == 86:
       k = chr(83)
   if i == 87:
       k = chr(10)
   if i == 88:
       k = chr(37)
   if i == 89:
       k = chr(3)
   if i == 90:
       k = chr(4)
   if i == 91:
       k = chr(89)
   if i == 92:
       k = chr(66)
   if i == 93:
       k = chr(51)
   if i == 94:
       k = chr(101)
   if i == 95:
       k = chr(117)
   if i == 96:
       k = chr(122)
   if i == 97:
       k = chr(95)
   if i == 98:
       k = chr(40)
   if i == 99:
       k = chr(86)
   if i == 100:
       k = chr(103)
   if i == 101:
       k = chr(116)
   if i == 102:
       k = chr(23)
   if i == 103:
       k = chr(120)
   if i == 104:
       k = chr(107)
   if i == 105:
       k = chr(105)
   if i == 106:
       k = chr(90)
   if i == 107:
       k = chr(81)
   if i == 108:
       k = chr(1)
   if i == 109:
       k = chr(16)
   if i == 110:
       k = chr(125)
   if i == 111:
       k = chr(109)
   if i == 112:
       k = chr(2)
   if i == 113:
       k = chr(49)
   if i == 114:
       k = chr(45)
   if i == 115:
       k = chr(47)
   if i == 116:
       k = chr(61)
   if i == 117:
       k = chr(115)
   if i == 118:
       k = chr(75)
   if i == 119:
       k = chr(118)
   if i == 120:
       k = chr(127)
   if i == 121:
       k = chr(20)
   if i == 122:
       k = chr(119)
   if i == 123:
       k = chr(62)
   if i == 124:
       k = chr(67)
   if i == 125:
       k = chr(77)
   if i == 126:
       k = chr(87)
   return k

def return_m(l):
   if l == 0:
       m = chr(56)
   if l == 1:
       m = chr(38)
   if l == 2:
       m = chr(94)
   if l == 3:
       m = chr(95)
   if l == 4:
       m = chr(6)
   if l == 5:
       m = chr(14)
   if l == 6:
       m = chr(31)
   if l == 7:
       m = chr(75)
   if l == 8:
       m = chr(13)
   if l == 9:
       m = chr(105)
   if l == 10:
       m = chr(29)
   if l == 11:
       m = chr(66)
   if l == 12:
       m = chr(47)
   if l == 13:
       m = chr(21)
   if l == 14:
       m = chr(109)
   if l == 15:
       m = chr(36)
   if l == 16:
       m = chr(77)
   if l == 17:
       m = chr(2)
   if l == 18:
       m = chr(12)
   if l == 19:
       m = chr(5)
   if l == 20:
       m = chr(87)
   if l == 21:
       m = chr(97)
   if l == 22:
       m = chr(93)
   if l == 23:
       m = chr(90)
   if l == 24:
       m = chr(119)
   if l == 25:
       m = chr(68)
   if l == 26:
       m = chr(0)
   if l == 27:
       m = chr(34)
   if l == 28:
       m = chr(62)
   if l == 29:
       m = chr(42)
   if l == 30:
       m = chr(67)
   if l == 31:
       m = chr(37)
   if l == 32:
       m = chr(65)
   if l == 33:
       m = chr(70)
   if l == 34:
       m = chr(112)
   if l == 35:
       m = chr(15)
   if l == 36:
       m = chr(35)
   if l == 37:
       m = chr(9)
   if l == 38:
       m = chr(114)
   if l == 39:
       m = chr(54)
   if l == 40:
       m = chr(117)
   if l == 41:
       m = chr(84)
   if l == 42:
       m = chr(127)
   if l == 43:
       m = chr(73)
   if l == 44:
       m = chr(100)
   if l == 45:
       m = chr(24)
   if l == 46:
       m = chr(111)
   if l == 47:
       m = chr(103)
   if l == 48:
       m = chr(121)
   if l == 49:
       m = chr(52)
   if l == 50:
       m = chr(98)
   if l == 51:
       m = chr(96)
   if l == 52:
       m = chr(45)
   if l == 53:
       m = chr(48)
   if l == 54:
       m = chr(91)
   if l == 55:
       m = chr(58)
   if l == 56:
       m = chr(30)
   if l == 57:
       m = chr(1)
   if l == 58:
       m = chr(25)
   if l == 59:
       m = chr(7)
   if l == 60:
       m = chr(72)
   if l == 61:
       m = chr(59)
   if l == 62:
       m = chr(40)
   if l == 63:
       m = chr(64) 
   if l == 64:
       m = chr(16)
   if l == 65:
       m = chr(107)
   if l == 66:
       m = chr(81)
   if l == 67:
       m = chr(8)
   if l == 68:
       m = chr(79)
   if l == 69:
       m = chr(86)
   if l == 70:
       m = chr(89)
   if l == 71:
       m = chr(82)
   if l == 72:
       m = chr(23)
   if l == 73:
       m = chr(55)
   if l == 74:
       m = chr(69)
   if l == 75:
       m = chr(28)
   if l == 76:
       m = chr(4)
   if l == 77:
       m = chr(110)
   if l == 78:
       m = chr(74)
   if l == 79:
       m = chr(60)
   if l == 80:
       m = chr(57)
   if l == 81:
       m = chr(63)
   if l == 82:
       m = chr(71)
   if l == 83:
       m = chr(85)
   if l == 84:
       m = chr(43)
   if l == 85:
       m = chr(120)
   if l == 86:
       m = chr(101)
   if l == 87:
       m = chr(49)
   if l == 88:
       m = chr(53)
   if l == 89:
       m = chr(51)
   if l == 90:
       m = chr(104)
   if l == 91:
       m = chr(92)
   if l == 92:
       m = chr(83)
   if l == 93:
       m = chr(118)
   if l == 94:
       m = chr(19)
   if l == 95:
       m = chr(123)
   if l == 96:
       m = chr(102)
   if l == 97:
       m = chr(3)
   if l == 98:
       m = chr(20)
   if l == 99:
       m = chr(39)
   if l == 100:
       m = chr(78)
   if l == 101:
       m = chr(18)
   if l == 102:
       m = chr(17)
   if l == 103:
       m = chr(41)
   if l == 104:
       m = chr(122)
   if l == 105:
       m = chr(88)
   if l == 106:
       m = chr(124)
   if l == 107:
       m = chr(80)
   if l == 108:
       m = chr(108)
   if l == 109:
       m = chr(44)
   if l == 110:
       m = chr(125)
   if l == 111:
       m = chr(27)
   if l == 112:
       m = chr(33)
   if l == 113:
       m = chr(32)
   if l == 114:
       m = chr(106)
   if l == 115:
       m = chr(10)
   if l == 116:
       m = chr(116)
   if l == 117:
       m = chr(126)
   if l == 118:
       m = chr(115)
   if l == 119:
       m = chr(22)
   if l == 120:
       m = chr(11)
   if l == 121:
       m = chr(46)
   if l == 122:
       m = chr(50)
   if l == 123:
       m = chr(26)
   if l == 124:
       m = chr(61)
   if l == 125:
       m = chr(76)
   if l == 126:
       m = chr(113)
   return m

def return_o(n):
   if n == 0:
       o = chr(88)
   if n == 1:
       o = chr(111)
   if n == 2:
       o = chr(71)
   if n == 3:
       o = chr(65)
   if n == 4:
       o = chr(13)
   if n == 5:
       o = chr(92)
   if n == 6:
       o = chr(93)
   if n == 7:
       o = chr(22)
   if n == 8:
       o = chr(68)
   if n == 9:
       o = chr(103)
   if n == 10:
       o = chr(11)
   if n == 11:
       o = chr(53)
   if n == 12:
       o = chr(4)
   if n == 13:
       o = chr(56)
   if n == 14:
       o = chr(60)
   if n == 15:
       o = chr(27)
   if n == 16:
       o = chr(52)
   if n == 17:
       o = chr(119)
   if n == 18:
       o = chr(115)
   if n == 19:
       o = chr(26)
   if n == 20:
       o = chr(3)
   if n == 21:
       o = chr(43)
   if n == 22:
       o = chr(9)
   if n == 23:
       o = chr(21)
   if n == 24:
       o = chr(17)
   if n == 25:
       o = chr(77)
   if n == 26:
       o = chr(90)
   if n == 27:
       o = chr(39)
   if n == 28:
       o = chr(114)
   if n == 29:
       o = chr(106)
   if n == 30:
       o = chr(55)
   if n == 31:
       o = chr(108)
   if n == 32:
       o = chr(82)
   if n == 33:
       o = chr(112)
   if n == 34:
       o = chr(50)
   if n == 35:
       o = chr(19)
   if n == 36:
       o = chr(12)
   if n == 37:
       o = chr(69)
   if n == 38:
       o = chr(123)
   if n == 39:
       o = chr(118)
   if n == 40:
       o = chr(86)
   if n == 41:
       o = chr(6)
   if n == 42:
       o = chr(33)
   if n == 43:
       o = chr(48)
   if n == 44:
       o = chr(124)
   if n == 45:
       o = chr(80)
   if n == 46:
       o = chr(78)
   if n == 47:
       o = chr(59)
   if n == 48:
       o = chr(83)
   if n == 49:
       o = chr(96)
   if n == 50:
       o = chr(126)
   if n == 51:
       o = chr(7)
   if n == 52:
       o = chr(46)
   if n == 53:
       o = chr(72)
   if n == 54:
       o = chr(104)
   if n == 55:
       o = chr(91)
   if n == 56:
       o = chr(35)
   if n == 57:
       o = chr(23)
   if n == 58:
       o = chr(36)
   if n == 59:
       o = chr(18)
   if n == 60:
       o = chr(5)
   if n == 61:
       o = chr(44)
   if n == 62:
       o = chr(110)
   if n == 63:
       o = chr(54)
   if n == 64:
       o = chr(42)
   if n == 65:
       o = chr(70)
   if n == 66:
       o = chr(102)
   if n == 67:
       o = chr(0)
   if n == 68:
       o = chr(81)
   if n == 69:
       o = chr(40)
   if n == 70:
       o = chr(41)
   if n == 71:
       o = chr(84)
   if n == 72:
       o = chr(74)
   if n == 73:
       o = chr(15)
   if n == 74:
       o = chr(116)
   if n == 75:
       o = chr(100)
   if n == 76:
       o = chr(121)
   if n == 77:
       o = chr(120)
   if n == 78:
       o = chr(20)
   if n == 79:
       o = chr(99)
   if n == 80:
       o = chr(45)
   if n == 81:
       o = chr(97)
   if n == 82:
       o = chr(30)
   if n == 83:
       o = chr(16)
   if n == 84:
       o = chr(31)
   if n == 85:
       o = chr(34)
   if n == 86:
       o = chr(49)
   if n == 87:
       o = chr(32)
   if n == 88:
       o = chr(89)
   if n == 89:
       o = chr(85)
   if n == 90:
       o = chr(63)
   if n == 91:
       o = chr(87)
   if n == 92:
       o = chr(109)
   if n == 93:
       o = chr(38)
   if n == 94:
       o = chr(1)
   if n == 95:
       o = chr(101)
   if n == 96:
       o = chr(28)
   if n == 97:
       o = chr(94)
   if n == 98:
       o = chr(62)
   if n == 99:
       o = chr(24)
   if n == 100:
       o = chr(75)
   if n == 101:
       o = chr(51)
   if n == 102:
       o = chr(125)
   if n == 103:
       o = chr(66)
   if n == 104:
       o = chr(107)
   if n == 105:
       o = chr(57)
   if n == 106:
       o = chr(67)
   if n == 107:
       o = chr(8)
   if n == 108:
       o = chr(79)
   if n == 109:
       o = chr(98)
   if n == 110:
       o = chr(122)
   if n == 111:
       o = chr(113)
   if n == 112:
       o = chr(2)
   if n == 113:
       o = chr(105)
   if n == 114:
       o = chr(47)
   if n == 115:
       o = chr(14)
   if n == 116:
       o = chr(58)
   if n == 117:
       o = chr(76)
   if n == 118:
       o = chr(25)
   if n == 119:
       o = chr(37)
   if n == 120:
       o = chr(29)
   if n == 121:
       o = chr(127)
   if n == 122:
       o = chr(117) 
   if n == 123:
       o = chr(73)
   if n == 124:
       o = chr(95)
   if n == 125:
       o = chr(61)
   if n == 126:
       o = chr(10)
   return o

def return_q(p):
   if p == 0:
       q = chr(9)
   if p == 1:
       q = chr(57)
   if p == 2:
       q = chr(97)
   if p == 3:
       q = chr(122)
   if p == 4:
       q = chr(81)
   if p == 5:
       q = chr(82)
   if p == 6:
       q = chr(35)
   if p == 7:
       q = chr(8)
   if p == 8:
       q = chr(103)
   if p == 9:
       q = chr(6)
   if p == 10:
       q = chr(54)
   if p == 11:
       q = chr(1)
   if p == 12:
       q = chr(64)
   if p == 13:
       q = chr(91)
   if p == 14:
       q = chr(32)
   if p == 15:
       q = chr(46)
   if p == 16:
       q = chr(99)
   if p == 17:
       q = chr(18)
   if p == 18:
       q = chr(14)
   if p == 19:
       q = chr(127)
   if p == 20:
       q = chr(56)
   if p == 21:
       q = chr(61)
   if p == 22:
       q = chr(31)
   if p == 23:
       q = chr(41)
   if p == 24:
       q = chr(44)
   if p == 25:
       q = chr(43)
   if p == 26:
       q = chr(45)
   if p == 27:
       q = chr(39)
   if p == 28:
       q = chr(59)
   if p == 29:
       q = chr(23)
   if p == 30:
       q = chr(113)
   if p == 31:
       q = chr(101)
   if p == 32:
       q = chr(110)
   if p == 33:
       q = chr(38)
   if p == 34:
       q = chr(98)
   if p == 35:
       q = chr(123)
   if p == 36:
       q = chr(4)
   if p == 37:
       q = chr(11)
   if p == 38:
       q = chr(52)
   if p == 39:
       q = chr(15)
   if p == 40:
       q = chr(125)
   if p == 41:
       q = chr(85)
   if p == 42:
       q = chr(47)
   if p == 43:
       q = chr(2)
   if p == 44:
       q = chr(37)
   if p == 45:
       q = chr(96)
   if p == 46:
       q = chr(116)
   if p == 47:
       q = chr(84)
   if p == 48:
       q = chr(27)
   if p == 49:
       q = chr(78)
   if p == 50:
       q = chr(75)
   if p == 51:
       q = chr(87)
   if p == 52:
       q = chr(88)
   if p == 53:
       q = chr(79)
   if p == 54:
       q = chr(49)
   if p == 55:
       q = chr(58)
   if p == 56:
       q = chr(42)
   if p == 57:
       q = chr(118)
   if p == 58:
       q = chr(0)
   if p == 59:
       q = chr(94)
   if p == 60:
       q = chr(86)
   if p == 61:
       q = chr(67)
   if p == 62:
       q = chr(19)
   if p == 63:
       q = chr(124)
   if p == 64:
       q = chr(104)
   if p == 65:
       q = chr(48)
   if p == 66:
       q = chr(29)
   if p == 67:
       q = chr(36)
   if p == 68:
       q = chr(16)
   if p == 69:
       q = chr(12)
   if p == 70:
       q = chr(100)
   if p == 71:
       q = chr(92)
   if p == 72:
       q = chr(50)
   if p == 73:
       q = chr(63)
   if p == 74:
       q = chr(120)
   if p == 75:
       q = chr(21)
   if p == 76:
       q = chr(95)
   if p == 77:
       q = chr(72)
   if p == 78:
       q = chr(83)
   if p == 79:
       q = chr(106)
   if p == 80:
       q = chr(102)
   if p == 81:
       q = chr(53)
   if p == 82:
       q = chr(22)
   if p == 83:
       q = chr(3)
   if p == 84:
       q = chr(5)
   if p == 85:
       q = chr(68)
   if p == 86:
       q = chr(73)
   if p == 87:
       q = chr(77)
   if p == 88:
       q = chr(109)
   if p == 89:
       q = chr(51)
   if p == 90:
       q = chr(74)
   if p == 91:
       q = chr(107)
   if p == 92:
       q = chr(90)
   if p == 93:
       q = chr(17)
   if p == 94:
       q = chr(126)
   if p == 95:
       q = chr(121)
   if p == 96:
       q = chr(89)
   if p == 97:
       q = chr(30)
   if p == 98:
       q = chr(114)
   if p == 99:
       q = chr(60)
   if p == 100:
       q = chr(20)
   if p == 101:
       q = chr(40)
   if p == 102:
       q = chr(80)
   if p == 103:
       q = chr(69)
   if p == 104:
       q = chr(65)
   if p == 105:
       q = chr(76)
   if p == 106:
       q = chr(71) 
   if p == 107:
       q = chr(105)
   if p == 108:
       q = chr(119)
   if p == 109:
       q = chr(13)
   if p == 110:
       q = chr(62)
   if p == 111:
       q = chr(28)
   if p == 112:
       q = chr(70)
   if p == 113:
       q = chr(7)
   if p == 114:
       q = chr(33)
   if p == 115:
       q = chr(112)
   if p == 116:
       q = chr(66)
   if p == 117:
       q = chr(10)
   if p == 118:
       q = chr(111)
   if p == 119:
       q = chr(93)
   if p == 120:
       q = chr(24)
   if p == 121:
       q = chr(26)
   if p == 122:
       q = chr(25)
   if p == 123:
       q = chr(108)
   if p == 124:
       q = chr(55)
   if p == 125:
       q = chr(115)
   if p == 126:
       q = chr(34)
   return q

def return_s(r):
   if r == 0:
       s = chr(52)
   if r == 1:
       s = chr(13)
   if r == 2:
       s = chr(16)
   if r == 3:
       s = chr(21)
   if r == 4:
       s = chr(37)
   if r == 5:
       s = chr(46)
   if r == 6:
       s = chr(117)
   if r == 7:
       s = chr(30)
   if r == 8:
       s = chr(29)
   if r == 9:
       s = chr(63)
   if r == 10:
       s = chr(106)
   if r == 11:
       s = chr(59)
   if r == 12:
       s = chr(24)
   if r == 13:
       s = chr(53)
   if r == 14:
       s = chr(126)
   if r == 15:
       s = chr(35)
   if r == 16:
       s = chr(36)
   if r == 17:
       s = chr(31)
   if r == 18:
       s = chr(92)
   if r == 19:
       s = chr(103)
   if r == 20:
       s = chr(105)
   if r == 21:
       s = chr(42)
   if r == 22:
       s = chr(110)
   if r == 23:
       s = chr(62)
   if r == 24:
       s = chr(102)
   if r == 25:
       s = chr(85)
   if r == 26:
       s = chr(61)
   if r == 27:
       s = chr(113)
   if r == 28:
       s = chr(19)
   if r == 29:
       s = chr(107)
   if r == 30:
       s = chr(4)
   if r == 31:
       s = chr(22)
   if r == 32:
       s = chr(20)
   if r == 33:
       s = chr(41)
   if r == 34:
       s = chr(122)
   if r == 35:
       s = chr(58)
   if r == 36:
       s = chr(70)
   if r == 37:
       s = chr(109)
   if r == 38:
       s = chr(87)
   if r == 39:
       s = chr(75)
   if r == 40:
       s = chr(54)
   if r == 41:
       s = chr(50)
   if r == 42:
       s = chr(47)
   if r == 43:
       s = chr(73)
   if r == 44:
       s = chr(45)
   if r == 45:
       s = chr(5)
   if r == 46:
       s = chr(77)
   if r == 47:
       s = chr(118)
   if r == 48:
       s = chr(88)
   if r == 49:
       s = chr(86)
   if r == 50:
       s = chr(3)
   if r == 51:
       s = chr(55)
   if r == 52:
       s = chr(125)
   if r == 53:
       s = chr(2)
   if r == 54:
       s = chr(7)
   if r == 55:
       s = chr(108)
   if r == 56:
       s = chr(95)
   if r == 57:
       s = chr(114)
   if r == 58:
       s = chr(94)
   if r == 59:
       s = chr(104)
   if r == 60:
       s = chr(56)
   if r == 61:
       s = chr(74)
   if r == 62:
       s = chr(43)
   if r == 63:
       s = chr(93)
   if r == 64:
       s = chr(89)
   if r == 65:
       s = chr(38)
   if r == 66:
       s = chr(33)
   if r == 67:
       s = chr(96)
   if r == 68:
       s = chr(82)
   if r == 69:
       s = chr(48)
   if r == 70:
       s = chr(83)
   if r == 71:
       s = chr(90)
   if r == 72:
       s = chr(32)
   if r == 73:
       s = chr(18)
   if r == 74:
       s = chr(120)
   if r == 75:
       s = chr(60)
   if r == 76:
       s = chr(68)
   if r == 77:
       s = chr(11)
   if r == 78:
       s = chr(12)
   if r == 79:
       s = chr(49)
   if r == 80:
       s = chr(127)
   if r == 81:
       s = chr(57)
   if r == 82:
       s = chr(15)
   if r == 83:
       s = chr(14)
   if r == 84:
       s = chr(101)
   if r == 85:
       s = chr(39)
   if r == 86:
       s = chr(44)
   if r == 87:
       s = chr(99)
   if r == 88:
       s = chr(26)
   if r == 89:
       s = chr(124)
   if r == 90:
       s = chr(100)
   if r == 91:
       s = chr(97)
   if r == 92:
       s = chr(28)
   if r == 93:
       s = chr(81)
   if r == 94:
       s = chr(80)
   if r == 95:
       s = chr(115)
   if r == 96:
       s = chr(119)
   if r == 97:
       s = chr(0)
   if r == 98:
       s = chr(67)
   if r == 99:
       s = chr(116)
   if r == 100:
       s = chr(51)
   if r == 101:
       s = chr(65)
   if r == 102:
       s = chr(40)
   if r == 103:
       s = chr(1)
   if r == 104:
       s = chr(123)
   if r == 105:
       s = chr(84)
   if r == 106:
       s = chr(121)
   if r == 107:
       s = chr(111)
   if r == 108:
       s = chr(91)
   if r == 109:
       s = chr(69)
   if r == 110:
       s = chr(27)
   if r == 111:
       s = chr(72) 
   if r == 112:
       s = chr(25)
   if r == 113:
       s = chr(64)
   if r == 114:
       s = chr(34)
   if r == 115:
       s = chr(98)
   if r == 116:
       s = chr(112)
   if r == 117:
       s = chr(17)
   if r == 118:
       s = chr(10)
   if r == 119:
       s = chr(6)
   if r == 120:
       s = chr(23)
   if r == 121:
       s = chr(78)
   if r == 122:
       s = chr(9)
   if r == 123:
       s = chr(76)
   if r == 124:
       s = chr(79)
   if r == 125:
       s = chr(8)
   if r == 126:
       s = chr(66)
   return s

def return_v(t):
   if t == 0:
       v = chr(125)
   if t == 1:
       v = chr(51)
   if t == 2:
       v = chr(52)
   if t == 3:
       v = chr(94)
   if t == 4:
       v = chr(119)
   if t == 5:
       v = chr(45)
   if t == 6:
       v = chr(23)
   if t == 7:
       v = chr(65)
   if t == 8:
       v = chr(30)
   if t == 9:
       v = chr(118)
   if t == 10:
       v = chr(20)
   if t == 11:
       v = chr(24)
   if t == 12:
       v = chr(19)
   if t == 13:
       v = chr(124)
   if t == 14:
       v = chr(115)
   if t == 15:
       v = chr(43)
   if t == 16:
       v = chr(90)
   if t == 17:
       v = chr(102)
   if t == 18:
       v = chr(106)
   if t == 19:
       v = chr(63)
   if t == 20:
       v = chr(122)
   if t == 21:
       v = chr(41)
   if t == 22:
       v = chr(69)
   if t == 23:
       v = chr(29)
   if t == 24:
       v = chr(35)
   if t == 25:
       v = chr(61)
   if t == 26:
       v = chr(3)
   if t == 27:
       v = chr(112)
   if t == 28:
       v = chr(81)
   if t == 29:
       v = chr(34)
   if t == 30:
       v = chr(67)
   if t == 31:
       v = chr(11)
   if t == 32:
       v = chr(120)
   if t == 33:
       v = chr(123)
   if t == 34:
       v = chr(113)
   if t == 35:
       v = chr(97)
   if t == 36:
       v = chr(116) 
   if t == 37:
       v = chr(60)
   if t == 38:
       v = chr(66)
   if t == 39:
       v = chr(87)
   if t == 40:
       v = chr(80)
   if t == 41:
       v = chr(126)
   if t == 42:
       v = chr(4)
   if t == 43:
       v = chr(127)
   if t == 44:
       v = chr(28)
   if t == 45:
       v = chr(2)
   if t == 46:
       v = chr(117)
   if t == 47:
       v = chr(25)
   if t == 48:
       v = chr(100)
   if t == 49:
       v = chr(110)
   if t == 50:
       v = chr(88)
   if t == 51:
       v = chr(18)
   if t == 52:
       v = chr(108)
   if t == 53:
       v = chr(17)
   if t == 54:
       v = chr(83)
   if t == 55:
       v = chr(75)
   if t == 56:
       v = chr(9)
   if t == 57:
       v = chr(31)
   if t == 58:
       v = chr(14)
   if t == 59:
       v = chr(44)
   if t == 60:
       v = chr(16)
   if t == 61:
       v = chr(114)
   if t == 62:
       v = chr(38)
   if t == 63:
       v = chr(15)
   if t == 64:
       v = chr(92)
   if t == 65:
       v = chr(1)
   if t == 66:
       v = chr(98)
   if t == 67:
       v = chr(59)
   if t == 68:
       v = chr(36)
   if t == 69:
       v = chr(21)
   if t == 70:
       v = chr(46)
   if t == 71:
       v = chr(104)
   if t == 72:
       v = chr(8)
   if t == 73:
       v = chr(86)
   if t == 74:
       v = chr(121)
   if t == 75:
       v = chr(84)
   if t == 76:
       v = chr(62)
   if t == 77:
       v = chr(58)
   if t == 78:
       v = chr(111)
   if t == 79:
       v = chr(105)
   if t == 80:
       v = chr(64)
   if t == 81:
       v = chr(85)
   if t == 82:
       v = chr(103)
   if t == 83:
       v = chr(32)
   if t == 84:
       v = chr(77)
   if t == 85:
       v = chr(95)
   if t == 86:
       v = chr(107)
   if t == 87:
       v = chr(82)
   if t == 88:
       v = chr(89)
   if t == 89:
       v = chr(99)
   if t == 90:
       v = chr(76)
   if t == 91:
       v = chr(39)
   if t == 92:
       v = chr(7)
   if t == 93:
       v = chr(73)
   if t == 94:
       v = chr(71)
   if t == 95:
       v = chr(48)
   if t == 96:
       v = chr(37)
   if t == 97:
       v = chr(42)
   if t == 98:
       v = chr(56)
   if t == 99:
       v = chr(109)
   if t == 100:
       v = chr(0)
   if t == 101:
       v = chr(101)
   if t == 102:
       v = chr(91)
   if t == 103:
       v = chr(12)
   if t == 104:
       v = chr(5)
   if t == 105:
       v = chr(78)
   if t == 106:
       v = chr(55)
   if t == 107:
       v = chr(54)
   if t == 108:
       v = chr(13)
   if t == 109:
       v = chr(68)
   if t == 110:
       v = chr(96)
   if t == 111:
       v = chr(26)
   if t == 112:
       v = chr(10)
   if t == 113:
       v = chr(33)
   if t == 114:
       v = chr(27)
   if t == 115:
       v = chr(22)
   if t == 116:
       v = chr(53)
   if t == 117:
       v = chr(47)
   if t == 118:
       v = chr(6)
   if t == 119:
       v = chr(74)
   if t == 120:
       v = chr(49)
   if t == 121:
       v = chr(93)
   if t == 122:
       v = chr(40)
   if t == 123:
       v = chr(70)
   if t == 124:
       v = chr(50)
   if t == 125:
       v = chr(57)
   if t == 126:
       v = chr(79)
   return v

def return_y(x):
   if x == 0:
       y = chr(68)
   if x == 1:
       y = chr(83)
   if x == 2:
       y = chr(90)
   if x == 3:
       y = chr(66)
   if x == 4:
       y = chr(44)
   if x == 5:
       y = chr(106)
   if x == 6:
       y = chr(39)
   if x == 7:
       y = chr(11)
   if x == 8:
       y = chr(117)
   if x == 9:
       y = chr(24)
   if x == 10:
       y = chr(10)
   if x == 11:
       y = chr(22)
   if x == 12:
       y = chr(32)
   if x == 13:
       y = chr(34)
   if x == 14:
       y = chr(84)
   if x == 15:
       y = chr(21)
   if x == 16:
       y = chr(5)
   if x == 17:
       y = chr(23)
   if x == 18:
       y = chr(35)
   if x == 19:
       y = chr(65)
   if x == 20:
       y = chr(50)
   if x == 21:
       y = chr(36)
   if x == 22:
       y = chr(120)
   if x == 23:
       y = chr(107)
   if x == 24:
       y = chr(89)
   if x == 25:
       y = chr(76)
   if x == 26:
       y = chr(51)
   if x == 27:
       y = chr(37)
   if x == 28:
       y = chr(14)
   if x == 29:
       y = chr(115)
   if x == 30:
       y = chr(7)
   if x == 31:
       y = chr(9)
   if x == 32:
       y = chr(2)
   if x == 33:
       y = chr(0)
   if x == 34:
       y = chr(80)
   if x == 35:
       y = chr(118)
   if x == 36:
       y = chr(123)
   if x == 37:
       y = chr(119)
   if x == 38:
       y = chr(100)
   if x == 39:
       y = chr(45)
   if x == 40:
       y = chr(127)
   if x == 41:
       y = chr(64)
   if x == 42:
       y = chr(27)
   if x == 43:
       y = chr(85)
   if x == 44:
       y = chr(31)
   if x == 45:
       y = chr(30)
   if x == 46:
       y = chr(42)
   if x == 47:
       y = chr(93)
   if x == 48:
       y = chr(63)
   if x == 49:
       y = chr(92)
   if x == 50:
       y = chr(69)
   if x == 51:
       y = chr(8)
   if x == 52:
       y = chr(4)
   if x == 53:
       y = chr(126)
   if x == 54:
       y = chr(86)
   if x == 55:
       y = chr(109)
   if x == 56:
       y = chr(95)
   if x == 57:
       y = chr(74)
   if x == 58:
       y = chr(103)
   if x == 59:
       y = chr(3)
   if x == 60:
       y = chr(121)
   if x == 61:
       y = chr(75)
   if x == 62:
       y = chr(67)
   if x == 63:
       y = chr(1)
   if x == 64:
       y = chr(38)
   if x == 65:
       y = chr(94)
   if x == 66:
       y = chr(113)
   if x == 67:
       y = chr(111)
   if x == 68:
       y = chr(60)
   if x == 69:
       y = chr(88)
   if x == 70:
       y = chr(43)
   if x == 71:
       y = chr(70)
   if x == 72:
       y = chr(125)
   if x == 73:
       y = chr(114)
   if x == 74:
       y = chr(47)
   if x == 75:
       y = chr(99)
   if x == 76:
       y = chr(62)
   if x == 77:
       y = chr(101)
   if x == 78:
       y = chr(73)
   if x == 79:
       y = chr(12)
   if x == 80:
       y = chr(57)
   if x == 81:
       y = chr(112)
   if x == 82:
       y = chr(110)
   if x == 83:
       y = chr(87)
   if x == 84:
       y = chr(16)
   if x == 85:
       y = chr(13)
   if x == 86:
       y = chr(46)
   if x == 87:
       y = chr(26)
   if x == 88:
       y = chr(122)
   if x == 89:
       y = chr(105)
   if x == 90:
       y = chr(71)
   if x == 91:
       y = chr(17)
   if x == 92:
       y = chr(108)
   if x == 93:
       y = chr(104)
   if x == 94:
       y = chr(82)
   if x == 95:
       y = chr(55)
   if x == 96:
       y = chr(33) 
   if x == 97:
       y = chr(19)
   if x == 98:
       y = chr(124)
   if x == 99:
       y = chr(18)
   if x == 100:
       y = chr(79)
   if x == 101:
       y = chr(56)
   if x == 102:
       y = chr(77)
   if x == 103:
       y = chr(72)
   if x == 104:
       y = chr(102)
   if x == 105:
       y = chr(29)
   if x == 106:
       y = chr(28)
   if x == 107:
       y = chr(6)
   if x == 108:
       y = chr(52)
   if x == 109:
       y = chr(97)
   if x == 110:
       y = chr(59)
   if x == 111:
       y = chr(48)
   if x == 112:
       y = chr(54)
   if x == 113:
       y = chr(15)
   if x == 114:
       y = chr(20)
   if x == 115:
       y = chr(96)
   if x == 116:
       y = chr(58)
   if x == 117:
       y = chr(98)
   if x == 118:
       y = chr(91)
   if x == 119:
       y = chr(53)
   if x == 120:
       y = chr(61)
   if x == 121:
       y = chr(78)
   if x == 122:
       y = chr(49)
   if x == 123:
       y = chr(81)
   if x == 124:
       y = chr(25)
   if x == 125:
       y = chr(40)
   if x == 126:
       y = chr(41)
   return y

def return_aa(z):
   if z == 0:
       aa = chr(43)
   if z == 1:
       aa = chr(8)
   if z == 2:
       aa = chr(116)
   if z == 3:
       aa = chr(67)
   if z == 4:
       aa = chr(21)
   if z == 5:
       aa = chr(85)
   if z == 6:
       aa = chr(92)
   if z == 7:
       aa = chr(19)
   if z == 8:
       aa = chr(104)
   if z == 9:
       aa = chr(37)
   if z == 10:
       aa = chr(2)
   if z == 11:
       aa = chr(11)
   if z == 12:
       aa = chr(76)
   if z == 13:
       aa = chr(123)
   if z == 14:
       aa = chr(87)
   if z == 15:
       aa = chr(83)
   if z == 16:
       aa = chr(100)
   if z == 17:
       aa = chr(63)
   if z == 18:
       aa = chr(72)
   if z == 19:
       aa = chr(119)
   if z == 20:
       aa = chr(121)
   if z == 21:
       aa = chr(64)
   if z == 22:
       aa = chr(81)
   if z == 23:
       aa = chr(102)
   if z == 24:
       aa = chr(26)
   if z == 25:
       aa = chr(5)
   if z == 26:
       aa = chr(86)
   if z == 27:
       aa = chr(91)
   if z == 28:
       aa = chr(59)
   if z == 29:
       aa = chr(17)
   if z == 30:
       aa = chr(50)
   if z == 31:
       aa = chr(106)
   if z == 32:
       aa = chr(127)
   if z == 33:
       aa = chr(39)
   if z == 34:
       aa = chr(28)
   if z == 35:
       aa = chr(93)
   if z == 36:
       aa = chr(107)
   if z == 37:
       aa = chr(98)
   if z == 38:
       aa = chr(89)
   if z == 39:
       aa = chr(71)
   if z == 40:
       aa = chr(110)
   if z == 41:
       aa = chr(69)
   if z == 42:
       aa = chr(13)
   if z == 43:
       aa = chr(90)
   if z == 44:
       aa = chr(51)
   if z == 45:
       aa = chr(25)
   if z == 46:
       aa = chr(120)
   if z == 47:
       aa = chr(4)
   if z == 48:
       aa = chr(35)
   if z == 49:
       aa = chr(40)
   if z == 50:
       aa = chr(29)
   if z == 51:
       aa = chr(27)
   if z == 52:
       aa = chr(60)
   if z == 53:
       aa = chr(1)
   if z == 54:
       aa = chr(20)
   if z == 55:
       aa = chr(96)
   if z == 56:
       aa = chr(57)
   if z == 57:
       aa = chr(56)
   if z == 58:
       aa = chr(47)
   if z == 59:
       aa = chr(9)
   if z == 60:
       aa = chr(18)
   if z == 61:
       aa = chr(15)
   if z == 62:
       aa = chr(61)
   if z == 63:
       aa = chr(6)
   if z == 64:
       aa = chr(122)
   if z == 65:
       aa = chr(44)
   if z == 66:
       aa = chr(36)
   if z == 67:
       aa = chr(48)
   if z == 68:
       aa = chr(74)
   if z == 69:
       aa = chr(125)
   if z == 70:
       aa = chr(118)
   if z == 71:
       aa = chr(65)
   if z == 72:
       aa = chr(68)
   if z == 73:
       aa = chr(80)
   if z == 74:
       aa = chr(113)
   if z == 75:
       aa = chr(88)
   if z == 76:
       aa = chr(31)
   if z == 77:
       aa = chr(62)
   if z == 78:
       aa = chr(103)
   if z == 79:
       aa = chr(114)
   if z == 80:
       aa = chr(10)
   if z == 81:
       aa = chr(97)
   if z == 82:
       aa = chr(75)
   if z == 83:
       aa = chr(78)
   if z == 84:
       aa = chr(22)
   if z == 85:
       aa = chr(14)
   if z == 86:
       aa = chr(49)
   if z == 87:
       aa = chr(101)
   if z == 88:
       aa = chr(117)
   if z == 89:
       aa = chr(45)
   if z == 90:
       aa = chr(84)
   if z == 91:
       aa = chr(105)
   if z == 92:
       aa = chr(3)
   if z == 93:
       aa = chr(94)
   if z == 94:
       aa = chr(109) 
   if z == 95:
       aa = chr(34)
   if z == 96:
       aa = chr(73)
   if z == 97:
       aa = chr(99)
   if z == 98:
       aa = chr(0)
   if z == 99:
       aa = chr(112)
   if z == 100:
       aa = chr(52)
   if z == 101:
       aa = chr(55)
   if z == 102:
       aa = chr(82)
   if z == 103:
       aa = chr(42)
   if z == 104:
       aa = chr(23)
   if z == 105:
       aa = chr(70)
   if z == 106:
       aa = chr(79)
   if z == 107:
       aa = chr(115)
   if z == 108:
       aa = chr(41)
   if z == 109:
       aa = chr(38)
   if z == 110:
       aa = chr(95)
   if z == 111:
       aa = chr(32)
   if z == 112:
       aa = chr(108)
   if z == 113:
       aa = chr(7)
   if z == 114:
       aa = chr(77)
   if z == 115:
       aa = chr(126)
   if z == 116:
       aa = chr(124)
   if z == 117:
       aa = chr(66)
   if z == 118:
       aa = chr(46)
   if z == 119:
       aa = chr(30)
   if z == 120:
       aa = chr(111)
   if z == 121:
       aa = chr(16)
   if z == 122:
       aa = chr(24)
   if z == 123:
       aa = chr(12)
   if z == 124:
       aa = chr(58)
   if z == 125:
       aa = chr(53)
   if z == 126:
       aa = chr(54)
   return aa

def return_ac(ab):
   if ab == 0:
       ac = chr(92)
   if ab == 1:
       ac = chr(39)
   if ab == 2:
       ac = chr(53)
   if ab == 3:
       ac = chr(100)
   if ab == 4:
       ac = chr(18)
   if ab == 5:
       ac = chr(1)
   if ab == 6:
       ac = chr(103)
   if ab == 7:
       ac = chr(125)
   if ab == 8:
       ac = chr(58)
   if ab == 9:
       ac = chr(86)
   if ab == 10:
       ac = chr(87)
   if ab == 11:
       ac = chr(43)
   if ab == 12:
       ac = chr(72)
   if ab == 13:
       ac = chr(64)
   if ab == 14:
       ac = chr(104)
   if ab == 15:
       ac = chr(69)
   if ab == 16:
       ac = chr(117)
   if ab == 17:
       ac = chr(42)
   if ab == 18:
       ac = chr(60)
   if ab == 19:
       ac = chr(54)
   if ab == 20:
       ac = chr(81)
   if ab == 21:
       ac = chr(55)
   if ab == 22:
       ac = chr(36)
   if ab == 23:
       ac = chr(73)
   if ab == 24:
       ac = chr(24)
   if ab == 25:
       ac = chr(3)
   if ab == 26:
       ac = chr(70)
   if ab == 27:
       ac = chr(118)
   if ab == 28:
       ac = chr(74)
   if ab == 29:
       ac = chr(48)
   if ab == 30:
       ac = chr(35)
   if ab == 31:
       ac = chr(31)
   if ab == 32:
       ac = chr(90)
   if ab == 33:
       ac = chr(96)
   if ab == 34:
       ac = chr(13)
   if ab == 35:
       ac = chr(108)
   if ab == 36:
       ac = chr(30)
   if ab == 37:
       ac = chr(106)
   if ab == 38:
       ac = chr(110)
   if ab == 39:
       ac = chr(22)
   if ab == 40:
       ac = chr(33)
   if ab == 41:
       ac = chr(111)
   if ab == 42:
       ac = chr(78)
   if ab == 43:
       ac = chr(101)
   if ab == 44:
       ac = chr(0)
   if ab == 45:
       ac = chr(63)
   if ab == 46:
       ac = chr(91)
   if ab == 47:
       ac = chr(127)
   if ab == 48:
       ac = chr(119)
   if ab == 49:
       ac = chr(51) 
   if ab == 50:
       ac = chr(97)
   if ab == 51:
       ac = chr(45)
   if ab == 52:
       ac = chr(7)
   if ab == 53:
       ac = chr(75)
   if ab == 54:
       ac = chr(38)
   if ab == 55:
       ac = chr(12)
   if ab == 56:
       ac = chr(19)
   if ab == 57:
       ac = chr(23)
   if ab == 58:
       ac = chr(57)
   if ab == 59:
       ac = chr(40)
   if ab == 60:
       ac = chr(124)
   if ab == 61:
       ac = chr(94)
   if ab == 62:
       ac = chr(95)
   if ab == 63:
       ac = chr(6)
   if ab == 64:
       ac = chr(4)
   if ab == 65:
       ac = chr(120)
   if ab == 66:
       ac = chr(107)
   if ab == 67:
       ac = chr(76)
   if ab == 68:
       ac = chr(5)
   if ab == 69:
       ac = chr(49)
   if ab == 70:
       ac = chr(89)
   if ab == 71:
       ac = chr(99)
   if ab == 72:
       ac = chr(8)
   if ab == 73:
       ac = chr(98)
   if ab == 74:
       ac = chr(71)
   if ab == 75:
       ac = chr(41)
   if ab == 76:
       ac = chr(66)
   if ab == 77:
       ac = chr(112)
   if ab == 78:
       ac = chr(14)
   if ab == 79:
       ac = chr(50)
   if ab == 80:
       ac = chr(79)
   if ab == 81:
       ac = chr(65)
   if ab == 82:
       ac = chr(9)
   if ab == 83:
       ac = chr(115)
   if ab == 84:
       ac = chr(114)
   if ab == 85:
       ac = chr(47)
   if ab == 86:
       ac = chr(20)
   if ab == 87:
       ac = chr(126)
   if ab == 88:
       ac = chr(116)
   if ab == 89:
       ac = chr(84)
   if ab == 90:
       ac = chr(83)
   if ab == 91:
       ac = chr(85)
   if ab == 92:
       ac = chr(16)
   if ab == 93:
       ac = chr(17)
   if ab == 94:
       ac = chr(46)
   if ab == 95:
       ac = chr(37)
   if ab == 96:
       ac = chr(67)
   if ab == 97:
       ac = chr(77)
   if ab == 98:
       ac = chr(121)
   if ab == 99:
       ac = chr(2)
   if ab == 100:
       ac = chr(44)
   if ab == 101:
       ac = chr(52)
   if ab == 102:
       ac = chr(25)
   if ab == 103:
       ac = chr(11)
   if ab == 104:
       ac = chr(122)
   if ab == 105:
       ac = chr(10)
   if ab == 106:
       ac = chr(21)
   if ab == 107:
       ac = chr(68)
   if ab == 108:
       ac = chr(27)
   if ab == 109:
       ac = chr(123)
   if ab == 110:
       ac = chr(59)
   if ab == 111:
       ac = chr(34)
   if ab == 112:
       ac = chr(56)
   if ab == 113:
       ac = chr(93)
   if ab == 114:
       ac = chr(82)
   if ab == 115:
       ac = chr(61)
   if ab == 116:
       ac = chr(29)
   if ab == 117:
       ac = chr(15)
   if ab == 118:
       ac = chr(102)
   if ab == 119:
       ac = chr(105)
   if ab == 120:
       ac = chr(62)
   if ab == 121:
       ac = chr(32)
   if ab == 122:
       ac = chr(80)
   if ab == 123:
       ac = chr(113)
   if ab == 124:
       ac = chr(28)
   if ab == 125:
       ac = chr(26)
   if ab == 126:
       ac = chr(88)
   return ac

def return_ae(ad):
   print(ad)
   if ad == 0:
       ae = chr(125) 
   if ad == 1:
       ae = chr(74)
   if ad == 2:
       ae = chr(56)
   if ad == 3:
       ae = chr(99)
   if ad == 4:
       ae = chr(79)
   if ad == 5:
       ae = chr(121)
   if ad == 6:
       ae = chr(110)
   if ad == 7:
       ae = chr(75)
   if ad == 8:
       ae = chr(70)
   if ad == 9:
       ae = chr(103)
   if ad == 10:
       ae = chr(15)
   if ad == 11:
       ae = chr(104)
   if ad == 12:
       ae = chr(95)
   if ad == 13:
       ae = chr(61)
   if ad == 14:
       ae = chr(90)
   if ad == 15:
       ae = chr(100)
   if ad == 16:
       ae = chr(115)
   if ad == 17:
       ae = chr(28)
   if ad == 18:
       ae = chr(108)
   if ad == 19:
       ae = chr(21)
   if ad == 20:
       ae = chr(93)
   if ad == 21:
       ae = chr(102)
   if ad == 22:
       ae = chr(30)
   if ad == 23:
       ae = chr(49)
   if ad == 24:
       ae = chr(66)
   if ad == 25:
       ae = chr(127)
   if ad == 26:
       ae = chr(97)
   if ad == 27:
       ae = chr(31)
   if ad == 28:
       ae = chr(113)
   if ad == 29:
       ae = chr(83)
   if ad == 30:
       ae = chr(65)
   if ad == 31:
       ae = chr(47)
   if ad == 32:
       ae = chr(119)
   if ad == 33:
       ae = chr(71)
   if ad == 34:
       ae = chr(77)
   if ad == 35:
       ae = chr(3)
   if ad == 36:
       ae = chr(19)
   if ad == 37:
       ae = chr(8)
   if ad == 38:
       ae = chr(11)
   if ad == 39:
       ae = chr(42)
   if ad == 40:
       ae = chr(50)
   if ad == 41:
       ae = chr(52)
   if ad == 42:
       ae = chr(25)
   if ad == 43:
       ae = chr(34)
   if ad == 44:
       ae = chr(101)
   if ad == 45:
       ae = chr(116)
   if ad == 46:
       ae = chr(114)
   if ad == 47:
       ae = chr(123)
   if ad == 48:
       ae = chr(20)
   if ad == 49:
       ae = chr(120)
   if ad == 50:
       ae = chr(81)
   if ad == 51:
       ae = chr(122)
   if ad == 52:
       ae = chr(117)
   if ad == 53:
       ae = chr(36)
   if ad == 54:
       ae = chr(88)
   if ad == 55:
       ae = chr(10)
   if ad == 56:
       ae = chr(0)
   if ad == 57:
       ae = chr(63)
   if ad == 58:
       ae = chr(73)
   if ad == 59:
       ae = chr(40)
   if ad == 60:
       ae = chr(16)
   if ad == 61:
       ae = chr(106)
   if ad == 62:
       ae = chr(86)
   if ad == 63:
       ae = chr(111)
   if ad == 64:
       ae = chr(23)
   if ad == 65:
       ae = chr(67)
   if ad == 66:
       ae = chr(107)
   if ad == 67:
       ae = chr(41)
   if ad == 68:
       ae = chr(112)
   if ad == 69:
       ae = chr(126)
   if ad == 70:
       ae = chr(26)
   if ad == 71:
       ae = chr(35)
   if ad == 72:
       ae = chr(55)
   if ad == 73:
       ae = chr(109)
   if ad == 74:
       ae = chr(85)
   if ad == 75:
       ae = chr(32)
   if ad == 76:
       ae = chr(37)
   if ad == 77:
       ae = chr(44)
   if ad == 78:
       ae = chr(43)
   if ad == 79:
       ae = chr(7)
   if ad == 80:
       ae = chr(33)
   if ad == 81:
       ae = chr(39)
   if ad == 82:
       ae = chr(58)
   if ad == 83:
       ae = chr(46)
   if ad == 84:
       ae = chr(2)
   if ad == 85:
       ae = chr(53)
   if ad == 86:
       ae = chr(72)
   if ad == 87:
       ae = chr(78)
   if ad == 88:
       ae = chr(45)
   if ad == 89:
       ae = chr(54)
   if ad == 90:
       ae = chr(68)
   if ad == 91:
       ae = chr(87)
   if ad == 92:
       ae = chr(59)
   if ad == 93:
       ae = chr(105)
   if ad == 94:
       ae = chr(98)
   if ad == 95:
       ae = chr(1)
   if ad == 96:
       ae = chr(91)
   if ad == 97:
       ae = chr(89)
   if ad == 98:
       ae = chr(22)
   if ad == 99:
       ae = chr(6)
   if ad == 100:
       ae = chr(17)
   if ad == 101:
       ae = chr(29)
   if ad == 102:
       ae = chr(124)
   if ad == 103:
       ae = chr(76)
   if ad == 104:
       ae = chr(27)
   if ad == 105:
       ae = chr(84)
   if ad == 106:
       ae = chr(4)
   if ad == 107:
       ae = chr(48)
   if ad == 108:
       ae = chr(18)
   if ad == 109:
       ae = chr(5)
   if ad == 110:
       ae = chr(24)
   if ad == 111:
       ae = chr(80)
   if ad == 112:
       ae = chr(96)
   if ad == 113:
       ae = chr(57)
   if ad == 114:
       ae = chr(118)
   if ad == 115:
       ae = chr(69)
   if ad == 116:
       ae = chr(94)
   if ad == 117:
       ae = chr(82)
   if ad == 118:
       ae = chr(14)
   if ad == 119:
       ae = chr(92)
   if ad == 120:
       ae = chr(62)
   if ad == 121:
       ae = chr(64)
   if ad == 122:
       ae = chr(13)
   if ad == 123:
       ae = chr(60)
   if ad == 124:
       ae = chr(38)
   if ad == 125:
       ae = chr(12)
   if ad == 126:
       ae = chr(9)
   return ae

print(return_b(random.randint(0,10000))+return_d(random.randint(0,10000))+return_f(random.randint(0,10000))+return_h(random.randint(0,10000))+return_k(random.randint(0,10000))+return_m(random.randint(0,10000))+return_o(random.randint(0,10000))+return_q(random.randint(0,10000))
      +return_s(random.randint(0,10000))+return_v(random.randint(0,10000))+return_y(random.randint(0,10000))+return_aa(random.randint(0,10000))+return_ac(random.randint(0,10000))+return_ae(random.randint(0,10000)))