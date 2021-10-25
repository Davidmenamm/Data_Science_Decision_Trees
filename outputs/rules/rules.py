def findDecision(obj): #obj[0]: Col42, obj[1]: Col26, obj[2]: Col40, obj[3]: Col6, obj[4]: Col24, obj[5]: Col15, obj[6]: Col14, obj[7]: Col16, obj[8]: Col4, obj[9]: Col10
	# {"feature": "Col26", "instances": 241, "metric_value": 0.7366, "depth": 1}
	if obj[1]>0.6773578557810922:
		# {"feature": "Col24", "instances": 147, "metric_value": 0.9113, "depth": 2}
		if obj[4]<=0.9552485845413384:
			# {"feature": "Col42", "instances": 146, "metric_value": 0.9065, "depth": 3}
			if obj[0]>0.6713838455206605:
				# {"feature": "Col10", "instances": 131, "metric_value": 0.9417, "depth": 4}
				if obj[9]<=0.9966807230825462:
					# {"feature": "Col40", "instances": 130, "metric_value": 0.9375, "depth": 5}
					if obj[2]>0.7135757915356931:
						# {"feature": "Col6", "instances": 118, "metric_value": 0.9647, "depth": 6}
						if obj[3]<=0.8167902440554151:
							# {"feature": "Col4", "instances": 117, "metric_value": 0.9612, "depth": 7}
							if obj[8]<=0.9973096348025565:
								# {"feature": "Col14", "instances": 116, "metric_value": 0.9576, "depth": 8}
								if obj[6]>0.5946693158657277:
									# {"feature": "Col15", "instances": 111, "metric_value": 0.9688, "depth": 9}
									if obj[5]>0.6096162681061396:
										# {"feature": "Col16", "instances": 108, "metric_value": 0.9751, "depth": 10}
										if obj[7]<=0.9676000888432529:
											return '0.5849056603773585'
										elif obj[7]>0.9676000888432529:
											return '1.0'
										else: return '1'
									elif obj[5]<=0.6096162681061396:
										return '1.0'
									else: return '1'
								elif obj[6]<=0.5946693158657277:
									return '1.0'
								else: return '1'
							elif obj[8]>0.9973096348025565:
								return '0'
							else: return '0'
						elif obj[3]>0.8167902440554151:
							return '0'
						else: return '0'
					elif obj[2]<=0.7135757915356931:
						return '1.0'
					else: return '1'
				elif obj[9]>0.9966807230825462:
					return '0'
				else: return '0'
			elif obj[0]<=0.6713838455206605:
				return '1.0'
			else: return '1'
		elif obj[4]>0.9552485845413384:
			return '0'
		else: return '0'
	elif obj[1]<=0.6773578557810922:
		# {"feature": "Col6", "instances": 94, "metric_value": 0.1485, "depth": 2}
		if obj[3]<=0.6980949152098528:
			return '1.0'
		elif obj[3]>0.6980949152098528:
			# {"feature": "Col40", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=0.8133333333333334:
				return '1.0'
			elif obj[2]>0.8133333333333334:
				return '0'
			else: return '0'
		else: return '1'
	else: return '1'
