class json_return:
    
    def __init__(self, total_cost, avg_cost_wo_gst, top_supplier_country):
        self.ret_json = {"totalCost": total_cost,
                         "avgCostWoGst": avg_cost_wo_gst,
                         "topSupplierCountry": top_supplier_country
                        }

    def get_json(self):
        return self.ret_json
