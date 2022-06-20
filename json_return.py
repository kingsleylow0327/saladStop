import errors


class json_return:
    def __init__(self,
                 total_cost,
                 avg_cost_wo_gst,
                 top_supplier_country,
                 error_code=0):

        if error_code == 0:
            self.ret_json = {"totalCost": total_cost,
                             "avgCostWoGst": avg_cost_wo_gst,
                             "topSupplierCountry": top_supplier_country}
        else:
            self.ret_json = errors.ERROR_MAP[error_code]

    def get_json(self):
        return self.ret_json
