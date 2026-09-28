from abc import ABC, abstractmethod


class Transporte(ABC):

    # Método Concreto: Comum a todas as filhas, já possui corpo lógico.
    def registrar_log(self, destino: str):
        print(f"[LOG CENTRAL] Iniciando cálculo de rota e custos para: {destino}")

    # Método Abstrato: Obriga todas as classes filhas a implementarem esta assinatura.
    @abstractmethod
    def calcular_frete(self, distancia_km: float, peso_kg: float) -> float:
        pass



class Caminhao(Transporte):


    def calcular_frete(self, distancia_km: float, peso_kg: float) -> float:
        # Regra de negócio: R$ 5,00 por Km + R$ 0,50 por kg de carga
        custo_total = (distancia_km * 5.0) + (peso_kg * 0.50)
        print(f"-> [CAMINHÃO] Processado. Custo final do frete: R$ {custo_total:.2f}")
        return custo_total


class Drone(Transporte):

    # Implementação obrigatória do contrato abstrato com validação específica
    def calcular_frete(self, distancia_km: float, peso_kg: float) -> float:
        # Regra de negócio: R$ 20,00 por Km, mas com limite de peso estrito de 2kg
        if peso_kg > 2.0:
            print(f"-> [DRONE] Operação cancelada: Carga de {peso_kg}kg excede o limite máximo de 2kg.")
            return 0.0

        custo_total = distancia_km * 20.0
        print(f"-> [DRONE] Processado. Custo final do frete: R$ {custo_total:.2f}")
        return custo_total



def processar_lote(lista_de_transportes: list, destino: str, distancia: float, peso: float):
    print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
    for item in lista_de_transportes:
        # Chama o método concreto herdado do pai
        item.registrar_log(destino)

        # Chama o método que era abstrato, mas que cada filha resolve à sua maneira
        item.calcular_frete(distancia_km=distancia, peso_kg=peso)
        print("-" * 40)



caminhao_01 = Caminhao()
drone_01 = Drone()


lote_leve = [caminhao_01, drone_01, caminhao_01]

processar_lote(lista_de_transportes=lote_leve, destino="Setor de Logística B", distancia=15.0, peso=1.5)


print("\n=== TESTE ADICIONAL: CARGA ACIMA DO LIMITE DO DRONE ===")
lote_pesado = [drone_01]
processar_lote(lista_de_transportes=lote_pesado, destino="Condomínio Central", distancia=10.0, peso=5.0)
