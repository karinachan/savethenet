# Copyright 2014 Google Inc. All Rights Reserved.
"""Code that's shared between multiple backend-services subcommands."""
from googlecloudsdk.calliope import arg_parsers


def AddUpdatableArgs(parser,
                     http_health_check_required,
                     default_timeout='30s',
                     default_port=80,
                     default_port_name='http'):
  """Adds top-level backend service arguments that can be updated."""
  parser.add_argument(
      '--description',
      help='An optional, textual description for the backend service.')

  http_health_checks = parser.add_argument(
      '--http-health-check',
      required=http_health_check_required,
      help=('An HTTP health check object for checking the health of '
            'the backend service.'))
  http_health_checks.detailed_help = """\
      An HTTP health check object for checking the health of the
      backend service.
        """

  timeout = parser.add_argument(
      '--timeout',
      default=default_timeout,
      type=arg_parsers.Duration(),
      help=('The amount of time to wait for a backend to respond to a '
            'request before considering the request failed.'))
  timeout.detailed_help = """\
      The amount of time to wait for a backend to respond to a request
      before considering the request failed. For example, specifying
      ``10s'' will give backends 10 seconds to respond to
      requests. Valid units for this flag are ``s'' for seconds, ``m''
      for minutes, and ``h'' for hours.
      """
  parser.add_argument(
      '--port',
      default=default_port,
      type=int,
      help='The TCP port to use when connected to the backend.')

  port_name = parser.add_argument(
      '--port-name',
      default=default_port_name,
      help=('A user-defined port name used to resolve which port to use on '
            'each backend.'))
  port_name.detailed_help = """\
      A user-defined port name used to resolve which port to use on
      each backend. ``--port'' will be deprecated soon and only
      port_name will be used. Port name will be matched to the
      (port_name, ports) specified in the resource view backend groups
      that are added to this backend service.  The port name should be
      RFC1035-labels compliant (e.g., ``http'', ``www1-static'').
      """
