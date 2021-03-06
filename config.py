
def headers():
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "4087",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.recompensas.pe",
        "Origin": "http://www.recompensas.pe",
        "Referer": "http://www.recompensas.pe/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    return headers

def payload(departamento,page):
    payload = {
    "title":"",
    "field_alias_value":"",
    "field_departamento_rq_tid":departamento,
    "field_provincia_rq_tid":"All",
    "field_grupo_tid":"All",
    "field_genero_tid":"All",
    "sort_by":"field_fecha_acta_value_1",
    "view_name":"profugos",
    "view_display_id":"page",
    "view_args":"",
    "view_path": "profugos",
    "view_base_path":"profugos",
    "view_dom_id":"3a5d8fe9ffa50c1e4065884ad42bec82",
    "pager_element":"0",
    "ajax_html_ids":[
    "skip-link",
    "block-views-social-block",
    "block-menu-menu-campanas",
    "btn-menu",
    "block-system-main-menu",
    "block-bean-banner-0",
    "block-views-exp-profugos-page",
    "views-exposed-form-profugos-page",
    "edit-title-wrapper",
    "edit-title",
    "edit-field-alias-value-wrapper",
    "edit-field-alias-value",
    "edit-field-departamento-rq-tid-wrapper",
    "edit-field-departamento-rq-tid",
    "edit-field-provincia-rq-tid-wrapper",
    "edit-field-provincia-rq-tid",
    "edit-field-grupo-tid-wrapper",
    "edit-field-grupo-tid",
    "edit-field-genero-tid-wrapper",
    "edit-field-genero-tid",
    "edit-submit-profugos",
    "edit-sort-by",
    "block-system-main",
    "block-block-1",
    "block-block-2",
    "block-block-7"
    ],
    "page": page,
    "ajax_page_state[theme]": "recompensas",
    "ajax_page_state[theme_token]": "pTEXt0in4Aj431jH-TSodI7rkyf-KtphO3d9gZaKzLc",
    "ajax_page_state[css][modules/system/system.base.css]": "1",
    "ajax_page_state[css][modules/system/system.menus.css]": "1",
    "ajax_page_state[css][modules/system/system.messages.css]": "1",
    "ajax_page_state[css][modules/system/system.theme.css]": "1",
    "ajax_page_state[css][modules/comment/comment.css]": "1",
    "ajax_page_state[css][sites/all/modules/contrib/date/date_api/date.css]": "1",
    "ajax_page_state[css][modules/field/theme/field.css]": "1",
    "ajax_page_state[css][modules/node/node.css]": "1",
    "ajax_page_state[css][modules/search/search.css]": "1",
    "ajax_page_state[css][modules/user/user.css]": "1",
    "ajax_page_state[css][sites/all/modules/contrib/youtube/css/youtube.css]": "1",
    "ajax_page_state[css][sites/all/modules/contrib/views/css/views.css]": "1",
    "ajax_page_state[css][sites/all/modules/contrib/ctools/css/ctools.css]": "1",
    "ajax_page_state[css][sites/all/themes/custom/recompensas/css/normalize.css]": "1",
    "ajax_page_state[css][sites/all/themes/custom/recompensas/css/font-awesome.css]": "1",
    "ajax_page_state[css][sites/all/themes/custom/recompensas/css/main.css]": "1",
    "ajax_page_state[css][sites/all/themes/custom/recompensas/css/media.css]": "1",
    "ajax_page_state[js][0]": "1",
    "ajax_page_state[js][sites/all/modules/contrib/jquery_update/replace/jquery/1.10/jquery.min.js]": "1",
    "ajax_page_state[js][misc/jquery.once.js]": "1",
    "ajax_page_state[js][misc/drupal.js]": "1",
    "ajax_page_state[js][sites/all/modules/contrib/jquery_update/replace/ui/external/jquery.cookie.js]": "1",
    "ajax_page_state[js][sites/all/modules/contrib/jquery_update/replace/misc/jquery.form.min.js]": "1",
    "ajax_page_state[js][misc/ajax.js]": "1",
    "ajax_page_state[js][sites/all/modules/contrib/jquery_update/js/jquery_update.js]": "1",
    "ajax_page_state[js][public://languages/es_KZnh0nBpzhrV5DjVZvV1Ip1LBH_m8W7vnSayc6iXdY0.js]": "1",
    "ajax_page_state[js][sites/all/modules/contrib/views/js/base.js]": "1",
    "ajax_page_state[js][misc/progress.js]": "1",
    "ajax_page_state[js][sites/all/modules/contrib/views/js/ajax_view.js]": "1",
    "ajax_page_state[js][sites/all/modules/contrib/google_analytics/googleanalytics.js]": "1",
    "ajax_page_state[js][sites/all/themes/custom/recompensas/js/main.js]": "1",
    "ajax_page_state[jquery_version]": "1.10"
    }
    return payload



