#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'marcos santos'
import os
from connect.conrequest import ConnectManager
from connect.conapi import ConnectApi
from common import connectool

class AppVersion(object):
    
    ## Create an app store version
    # app_id App id
    # version_string Version like '1.0.0'
    # copyright Proprietary company or person
    # build_id Build id related to the version
    # release_type Possible values: MANUAL, AFTER_APPROVAL, SCHEDULED
    # platform Possible values: IOS, MAC_OS, TV_OS
    # earliest_release_date Date-time
    # uses_idfa If app uses IDFA
    @classmethod
    def create_app_version(cls, app_id, version_string, platform = 'IOS',
                            release_type = 'MANUAL', copyright = None, build_id = None,
                            earliest_release_date = None, uses_idfa = False):
        result = ConnectManager().create_app_version(ConnectApi.connect_api_app_versions.value[0],
                                                    app_id = app_id, version_string = version_string, platform = platform,
                                                    release_type = release_type, copyright = copyright, build_id = build_id,
                                                    earliest_release_date = earliest_release_date, uses_idfa = uses_idfa)
        if result['status'] == 201:
            return {'status': 200, 'data': result['data']}
        return result
    
    ## Query App version localized info
    # id App version id
    @classmethod
    def get_app_version_localizations(cls, id):
        return ConnectManager().get_app_version_localizations(ConnectApi.connect_api_app_versions.value[0], id)