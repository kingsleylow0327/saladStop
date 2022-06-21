import errors


class JsonReturn:
    def __init__(self,
                 total_cost,
                 avg_cost_wo_gst,
                 top_supplier_country,
                 error_code=0):

        if error_code == 0:
            self.ret_json = {"totalCost": "{:.2f}".format(float(total_cost)),
                             "avgCostWoGst": "{:.2f}".format(float(avg_cost_wo_gst)),  # noqa: E501
                             "topSupplierCountry": top_supplier_country}
        else:
            self.ret_json = errors.ERROR_MAP[error_code]

    def get_json(self):
        return self.ret_json
