def findDecision(obj): #obj[0]: Col42, obj[1]: Col26, obj[2]: Col40, obj[3]: Col6, obj[4]: Col24, obj[5]: Col15, obj[6]: Col14
	# {"feature": "Col26", "instances": 382, "metric_value": 1.0, "depth": 1}
	if obj[1]>0.5557020004986393:
		# {"feature": "Col40", "instances": 321, "metric_value": 0.9738, "depth": 2}
		if obj[2]>0.7340274040674959:
			# {"feature": "Col42", "instances": 288, "metric_value": 0.9217, "depth": 3}
			if obj[0]>0.6528887052747431:
				# {"feature": "Col24", "instances": 280, "metric_value": 0.902, "depth": 4}
				if obj[4]>0.4270447585270152:
					# {"feature": "Col14", "instances": 278, "metric_value": 0.8965, "depth": 5}
					if obj[6]>0.5769230769230769:
						# {"feature": "Col6", "instances": 276, "metric_value": 0.8908, "depth": 6}
						if obj[3]>0.453125:
							# {"feature": "Col15", "instances": 275, "metric_value": 0.8879, "depth": 7}
							if obj[5]>0.4814814814814815:
								return '0.3029197080291971'
							elif obj[5]<=0.4814814814814815:
								return '1.0'
							else: return '1'
						elif obj[3]<=0.453125:
							return '1.0'
						else: return '1'
					elif obj[6]<=0.5769230769230769:
						return '1.0'
					else: return '1'
				elif obj[4]<=0.4270447585270152:
					return '1.0'
				else: return '1'
			elif obj[0]<=0.6528887052747431:
				return '1.0'
			else: return '1'
		elif obj[2]<=0.7340274040674959:
			return '1.0'
		else: return '1'
	elif obj[1]<=0.5557020004986393:
		return '1.0'
	else: return '1'
