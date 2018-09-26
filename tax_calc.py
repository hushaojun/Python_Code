# -*- coding: utf-8 -*-

def new_tax(original_income, personal_free):
	free_amount = 5000.0
	free_amount = free_amount + float(personal_free)	#扣除社保基数
	original_income = float(original_income)
	charge_amount = 0.0
	
	if original_income > free_amount:
		income_minus_free = original_income - free_amount	#扣去起征点后收入
		if income_minus_free > 3000.0:	#级数1
			charge_amount = charge_amount + 3000 * 0.03
			level1_free = income_minus_free - 3000.0
			if level1_free > 9000.0:	#级数2	12000
				charge_amount = charge_amount + 9000.0 * 0.1
				level2_free = level1_free - 9000.0
				if level2_free > 13000.0:	#级数3	25000
					charge_amount = charge_amount + 13000.0 * 0.2
					level3_free = level2_free - 13000.0
					if level3_free > 10000.0:	#级数4	35000
						charge_amount = charge_amount + 10000.0 * 0.25
						level4_free = level3_free - 10000.0
						if level4_free > 20000.0:	#级数5	55000
							charge_amount = charge_amount + 20000.0 * 0.3
							level5_free = level4_free - 20000.0
							if level5_free > 25000.0:	#级数6	80000
								charge_amount = charge_amount + 25000.0 * 0.35
								level6_free = level5_free - 25000.0
								charge_amount = charge_amount + level6_free * 0.45
							else:
								charge_amount = charge_amount + level5_free * 0.35
						else:
							charge_amount = charge_amount + level4_free * 0.3
					else:
						charge_amount = charge_amount + level3_free * 0.25
				else:
					charge_amount = charge_amount + level2_free * 0.2
			else:
				charge_amount = charge_amount + level1_free * 0.1
		else:
			charge_amount = charge_amount + income_minus_free * 0.03
	else:
		pass
		
	print('新个税算法下%s税前收入应交税：%s' % (original_income, charge_amount))
	
def old_tax(original_income, personal_free):
	free_amount = 3500.0
	free_amount = free_amount + float(personal_free)	#扣除社保基数
	original_income = float(original_income)
	charge_amount = 0.0
	
	if original_income > free_amount:
		income_minus_free = original_income - free_amount	#扣去起征点后收入
		if income_minus_free > 1500.0:	#级数1
			charge_amount = charge_amount + 1500 * 0.03
			level1_free = income_minus_free - 1500.0
			if level1_free > 3000.0:	#级数2	4500
				charge_amount = charge_amount + 3000.0 * 0.1
				level2_free = level1_free - 3000.0
				if level2_free > 4500.0:	#级数3	9000
					charge_amount = charge_amount + 4500.0 * 0.2
					level3_free = level2_free - 4500.0
					if level3_free > 24000.0:	#级数4	35000
						charge_amount = charge_amount + 24000.0 * 0.25
						level4_free = level3_free - 24000.0
						if level4_free > 20000.0:	#级数5	55000
							charge_amount = charge_amount + 20000.0 * 0.3
							level5_free = level4_free - 20000.0
							if level5_free > 25000.0:	#级数6	80000
								charge_amount = charge_amount + 25000.0 * 0.35
								level6_free = level5_free - 25000.0
								charge_amount = charge_amount + level6_free * 0.45
							else:
								charge_amount = charge_amount + level5_free * 0.35
						else:
							charge_amount = charge_amount + level4_free * 0.3
					else:
						charge_amount = charge_amount + level3_free * 0.25
				else:
					charge_amount = charge_amount + level2_free * 0.2
			else:
				charge_amount = charge_amount + level1_free * 0.1
		else:
			charge_amount = charge_amount + income_minus_free * 0.03
	else:
		pass
		
	print('旧个税算法下%s税前收入应交税：%s' % (original_income, charge_amount))
	
if __name__ == '__main__':
	while True:
		total_incomme = float(input('税前工资为：'))
		social_security = float(input('五险一金总数为：'))
		new_tax(total_incomme, social_security)
		old_tax(total_incomme, social_security)
		exit = input('是否退出(Y/y)：')
		if (exit == 'Y') or (exit == 'y'):
			break
