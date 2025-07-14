# Thunder/bot/clients.py

import asyncio
from Thunder.bot import StreamBot
from Thunder.utils.handler import handle_flood_wait
from Thunder.utils.logger import logger

async def cleanup_clients():
    try:
        await handle_flood_wait(StreamBot.stop)
        print("✓ Primary client stopped successfully")
    except Exception as e:
        logger.error(f"Error stopping primary client: {e}", exc_info=True)

async def initialize_clients():
    print("╠══════════════════ INITIALIZING BOT ═══════════════════╣")
    try:
        await handle_flood_wait(StreamBot.start)
        print("✓ StreamBot started successfully")
    except Exception as e:
        logger.error(f"✖ Failed to start StreamBot: {e}", exc_info=True)
        raise e

  #  async def start_client(client_id, token):
   #     try:
      #      if client_id == len(all_tokens):
    #            await asyncio.sleep(2)
       #     client = Client(
          #      api_hash=Var.API_HASH,
       #         api_id=Var.API_ID,
     #           bot_token=token,
       #         in_memory=True,
       #         name=str(client_id),
       #         no_updates=True,
        #        sleep_threshold=Var.SLEEP_THRESHOLD
        #    )
       #     await handle_flood_wait(client.start)
      #      work_loads[client_id] = 0
     #       print(f"   ◎ Client ID {client_id} started")
     #       return client_id, client
   #     except Exception as e:
#      *      logger.error(f"   ✖ Failed to start Client ID {client_id}. Error: {e}", exc_info=True)
#     *       return None 

#    clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items() if token])
#    clients = [client for client in clients if client]
#
#    multi_clients.update(dict(clients))
    
#    if len(multi_clients) > 1:
#        Var.MULTI_CLIENT = True
 #       print("╠══════════════════════ MULTI-CLIENT ═══════════════════════╣")
#        print(f"   ◎ Total Clients: {len(multi_clients)} (Including primary client)")
        
 #       print("   ▶ Initial workload distribution:")
 #       for client_id, load in work_loads.items():
#            print(f"   • Client {client_id}: {load} tasks")
            
#    else:
   #     print("╠═══════════════════════════════════════════════════════════╣")
   #     print("   ▶ No additional clients were initialized")
   #     print("   ▶ Primary client will handle all requests")
