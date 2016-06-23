/**
 * Created by Mesogene on 2015/3/19.
 */
 $(function () {
        $('#basic-events-table').next().click(function () {
            $(this).hide();
            var $result = $('#events-result');

            $('#events-table').bootstrapTable({
                }).on('all.bs.table', function (e, name, args) {
                console.log('Event:', name, ', data:', args);
            }).on('click-row.bs.table', function (e, row, $element) {
                $result.text('Event: click-row.bs.table, data: ' + JSON.stringify(row));
            }).on('dbl-click-row.bs.table', function (e, row, $element) {
                $result.text('Event: dbl-click-row.bs.table, data: ' + JSON.stringify(row));
            }).on('sort.bs.table', function (e, name, order) {
                $result.text('Event: sort.bs.table, data: ' + name + ', ' + order);
            }).on('check.bs.table', function (e, row) {
                $result.text('Event: check.bs.table, data: ' + JSON.stringify(row));
            }).on('uncheck.bs.table', function (e, row) {
                $result.text('Event: uncheck.bs.table, data: ' + JSON.stringify(row));
            }).on('check-all.bs.table', function (e) {
                $result.text('Event: check-all.bs.table');
            }).on('uncheck-all.bs.table', function (e) {
                $result.text('Event: uncheck-all.bs.table');
            }).on('load-success.bs.table', function (e, data) {
                $result.text('Event: load-success.bs.table');
            }).on('load-error.bs.table', function (e, status) {
                $result.text('Event: load-error.bs.table, data: ' + status);
            }).on('column-switch.bs.table', function (e, field, checked) {
                $result.text('Event: column-switch.bs.table, data: ' +
                    field + ', ' + checked);
            }).on('page-change.bs.table', function (e, size, number) {
                $result.text('Event: page-change.bs.table, data: ' + number + ', ' + size);
            }).on('search.bs.table', function (e, text) {
                $result.text('Event: search.bs.table, data: ' + text);
            });
        });
    });
