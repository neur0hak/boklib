# boklib

usage

    from boklib import bok

    api_key = 'example' # get an api key in this site: https://ecos.bok.or.kr/jsp/openapi/OpenApiController.jsp?t=main
    lang = '' # 'kr'or 'en'
    state_code = '' # get a state_code in table_list or get a state_code in item_list
    cycle = '' # get a cycle in item_list
    start_date = '' # get a start_date in item_list
    end_date = '' # get a end_date in item_list
    item_code = '' # get a item_code in item_list

    bok = bok(api_key, lang)
    result_key_list = bok.key_List()
    result_table_list = bok.table_list()
    result_item_list = bok.item_list(stat_code)
    result_search = bok.search(stat_code, cycle, start_date, end_date, item_code)
    result_meta = bok.meta(meta_search_word) # maybe korean language only - site: https://ecos.bok.or.kr/jsp/use/metadata/MetaData.jsp
    result_word = bok.word(search_word) # maybe korean language only - site: https://ecos.bok.or.kr/jsp/use/metaword/MetaDataWordList.jsp

    for result in result_key_list['row']:
      class_name =  result['CLASS_NAME']
      keystat_name = result['KEYSTAT_NAME']
      data_value = result['DATA_VALUE']
      cycle = result['CYCLE']
      unit_name = result['UNIT_NAME']
      print('class_name = %s, keystat_name = %s, data_value = %s, cycle = %s, unit_name = %s' % (class_name, keystat_name, data_value, cycle, unit_name))

    #
    # --- result example ---
    # {'list_total_count': {}, 'row' : [] }
    #
    # print result_key_list
    # {'list_total_count' : 1, 'row' : [{'CLASS_NAME' : '', 'KEYSTAT_NAME' : '', 'DATA_VALUE' : '', 'CYCLE' : '', 'UNIT_NAME' : ''}]}
    #
    # print result_table_list
    # {'list_total_count': 1, 'row' : [{'P_STAT_CODE' : '', 'STAT_CODE' : '', 'STAT_NAME' : '', 'CYCLE' : '', 'SRCH_YN' : '', 'ORG_NAME' : ''}] }
    #
    # print result_item_list
    # {'list_total_count' : 1, 'row' : [{'STAT_CODE' : '', 'STAT_NAME' : '', 'GRP_CODE' : '', 'GRP_NAME' : '', 'P_ITEM_CODE' : '', 'ITEM_CODE' : '', 'ITEM_NAME' : '', 'CYCLE' : '', 'START_TIME' : '', 'END_TIME' : '', 'DATA_CNT' : ''}]}
    # print result_search
    # {'list_total_count' : 1, 'row' : [{'STAT_CODE' : '', 'STAT_NAME' : '', 'ITEM_CODE1' : '', 'ITEM_CODE2' : '', 'ITEM_CODE3' : '', 'UNIT_NAME' : '', 'TIME' : '', 'DATA_VALUE' : ''}]}
    #
    # print result_meta
    # {'list_total_count': 1, 'row' : [{'LVL' : '', 'P_CONT_CODE' : '', 'CONT_CODE' : '', 'CONT_NAME' : '', 'META_DATA' : ''}] }
    #
    # print result_word
    # {'list_total_count': 1, 'row' : [{'WORD' : '', 'CONTENT' : ''}] }
    #
