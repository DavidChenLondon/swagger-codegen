# coding: utf-8

"""
    Nomad Hawk

    This is the API descriptor for the Nomad Hawk API, responsible for tracking and analytics.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: paul@samarkand.global
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TrackApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def track(self, body, **kwargs):  # noqa: E501
        """Record an individual event  # noqa: E501

        Sends an event to hawk  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.track(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Event body: Event to track (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.track_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.track_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def track_with_http_info(self, body, **kwargs):  # noqa: E501
        """Record an individual event  # noqa: E501

        Sends an event to hawk  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.track_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Event body: Event to track (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method track" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `track`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/track', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def track_0(self, body, store_id, **kwargs):  # noqa: E501
        """Record an individual event  # noqa: E501

        Sends an event to hawk  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.track_0(body, store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Event body: Event to track (required)
        :param str store_id: Store id of tracked event (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.track_0_with_http_info(body, store_id, **kwargs)  # noqa: E501
        else:
            (data) = self.track_0_with_http_info(body, store_id, **kwargs)  # noqa: E501
            return data

    def track_0_with_http_info(self, body, store_id, **kwargs):  # noqa: E501
        """Record an individual event  # noqa: E501

        Sends an event to hawk  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.track_0_with_http_info(body, store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Event body: Event to track (required)
        :param str store_id: Store id of tracked event (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'store_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method track_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `track_0`")  # noqa: E501
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `track_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['store_id'] = params['store_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/track/{store_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
