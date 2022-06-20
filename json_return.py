class json_return:

    def __init__(self, total_cost, avg_cost_wo_gst, top_supplier_country, error_code=0):
        if error_code == 0:
            self.ret_json = {"totalCost": total_cost,
                             "avgCostWoGst": avg_cost_wo_gst,
                             "topSupplierCountry": top_supplier_country
                            }
        elif error_code == -1:
            self.ret_json = {"error": "No data within this date range"
                            }

    def get_json(self):
        return self.ret_json
