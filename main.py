from logic import WsConnection, TomHelper
from models import Block
from models import Response
import asyncio



async def main():
    ws_connection =  WsConnection("209.126.82.146", 8080, 0.11)
    tom_helper = TomHelper(ws_connection, Response(), Block())
    await tom_helper()    
        #responses = await asyncio.gather(tom_helper.get_responses())

def start():
    asyncio.run(main())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

#if __name__ == '__main__':
#    scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 10000})
#    scheduler.add_job(start, 'interval', seconds=0.1)
#    scheduler.start()
#    #start()
#    try:
#        while True:
#            time.sleep(2)
#    except (KeyboardInterrupt, SystemExit):
#        #pass
#        scheduler.shutdown()
