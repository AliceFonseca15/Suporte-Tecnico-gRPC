"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import suporte_pb2 as suporte__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in suporte_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ServicoSuporteStub(object):

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AbrirChamado = channel.unary_unary(
                '/suporte.ServicoSuporte/AbrirChamado',
                request_serializer=suporte__pb2.Chamado.SerializeToString,
                response_deserializer=suporte__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.ConsultarChamado = channel.unary_unary(
                '/suporte.ServicoSuporte/ConsultarChamado',
                request_serializer=suporte__pb2.IdRequest.SerializeToString,
                response_deserializer=suporte__pb2.Chamado.FromString,
                _registered_method=True)
        self.ListarChamados = channel.unary_unary(
                '/suporte.ServicoSuporte/ListarChamados',
                request_serializer=suporte__pb2.Empty.SerializeToString,
                response_deserializer=suporte__pb2.ListaChamados.FromString,
                _registered_method=True)
        self.AtualizarChamado = channel.unary_unary(
                '/suporte.ServicoSuporte/AtualizarChamado',
                request_serializer=suporte__pb2.Chamado.SerializeToString,
                response_deserializer=suporte__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.ResolverChamado = channel.unary_unary(
                '/suporte.ServicoSuporte/ResolverChamado',
                request_serializer=suporte__pb2.IdRequest.SerializeToString,
                response_deserializer=suporte__pb2.StatusResponse.FromString,
                _registered_method=True)


class ServicoSuporteServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AbrirChamado(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsultarChamado(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListarChamados(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AtualizarChamado(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResolverChamado(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServicoSuporteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AbrirChamado': grpc.unary_unary_rpc_method_handler(
                    servicer.AbrirChamado,
                    request_deserializer=suporte__pb2.Chamado.FromString,
                    response_serializer=suporte__pb2.StatusResponse.SerializeToString,
            ),
            'ConsultarChamado': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarChamado,
                    request_deserializer=suporte__pb2.IdRequest.FromString,
                    response_serializer=suporte__pb2.Chamado.SerializeToString,
            ),
            'ListarChamados': grpc.unary_unary_rpc_method_handler(
                    servicer.ListarChamados,
                    request_deserializer=suporte__pb2.Empty.FromString,
                    response_serializer=suporte__pb2.ListaChamados.SerializeToString,
            ),
            'AtualizarChamado': grpc.unary_unary_rpc_method_handler(
                    servicer.AtualizarChamado,
                    request_deserializer=suporte__pb2.Chamado.FromString,
                    response_serializer=suporte__pb2.StatusResponse.SerializeToString,
            ),
            'ResolverChamado': grpc.unary_unary_rpc_method_handler(
                    servicer.ResolverChamado,
                    request_deserializer=suporte__pb2.IdRequest.FromString,
                    response_serializer=suporte__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'suporte.ServicoSuporte', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('suporte.ServicoSuporte', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ServicoSuporte(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AbrirChamado(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/suporte.ServicoSuporte/AbrirChamado',
            suporte__pb2.Chamado.SerializeToString,
            suporte__pb2.StatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ConsultarChamado(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/suporte.ServicoSuporte/ConsultarChamado',
            suporte__pb2.IdRequest.SerializeToString,
            suporte__pb2.Chamado.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListarChamados(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/suporte.ServicoSuporte/ListarChamados',
            suporte__pb2.Empty.SerializeToString,
            suporte__pb2.ListaChamados.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AtualizarChamado(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/suporte.ServicoSuporte/AtualizarChamado',
            suporte__pb2.Chamado.SerializeToString,
            suporte__pb2.StatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResolverChamado(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/suporte.ServicoSuporte/ResolverChamado',
            suporte__pb2.IdRequest.SerializeToString,
            suporte__pb2.StatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
