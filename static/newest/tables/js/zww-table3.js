/**
 * Created by Mesogene on 2015/4/6.
 */
/*****************************************饮食信息表格**************************************************************/
$('#sample-table-food').bootstrapTable({
    sidePagination:'server',
    queryParamsType:'limit',
    responseHandler:function(res) {
        return {
            rows:res.results,
            total:res.count
        }
    },
    queryParams:function queryParams(params){
        return {
            "page":(params.offset/params.limit)+1,
            "page_size":params.limit
        };
    }
});
/*****************************************运动信息表格**************************************************************/
$('#sample-table-sport').bootstrapTable({
    sidePagination:'server',
    queryParamsType:'limit',
    responseHandler:function(res) {
        return {
            rows:res.results,
            total:res.count
        }
    },
    queryParams:function queryParams(params){
        return {
            "page":(params.offset/params.limit)+1,
            "page_size":params.limit
        };
    }
});
/*****************************************睡眠信息表格**************************************************************/
$('#sample-table-sleep').bootstrapTable({
    sidePagination:'server',
    queryParamsType:'limit',
    responseHandler:function(res) {
        return {
            rows:res.results,
            total:res.count
        }
    },
    queryParams:function queryParams(params){
        return {
            "page":(params.offset/params.limit)+1,
            "page_size":params.limit
        };
    }
});
function detail(){
    return '<a><span class="glyphicon glyphicon-eye-open"></span></a>';
}
