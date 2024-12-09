
# Estratégias de Monitoramento neste projeto

## Como uma melhoria você implementaria o monitoramento desse fluxo? 
## Quais são os pontos criticos?  

### Pontos Críticos e Monitoramento

#### Pontos Críticos

1. **Latência e Tempo de Execução**:
   - Monitore a latência das execuções da Lambda.
   - Monitore a latência de leitura/gravação no DynamoDB.

2. **Taxa de Erros**:
   - Verifique a taxa de erros das invocações da Lambda.
   - Monitore mensagens falhadas ou não entregues no S3, SNS e SQS.

3. **Escalabilidade**:
   - Monitore a utilização de leitura e escrita no DynamoDB.
   - Verifique se as filas SQS não estão se tornando gargalos.

#### Monitoramento

1. **Amazon CloudWatch**:
   - Logs, métricas e alarmes configurados.
 - 
2. **AWS X-Ray**:
   - Rastreamento detalhado das solicitações. // não aplicados no momento desse projeto
   - 
3. **AWS CloudTrail**:
   - Auditoria e log de chamadas de API. // não aplicados no momento desse projeto