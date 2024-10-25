from sqlalchemy import select
from CarinfoModel import CarinfoModel
from sqlalchemy import and_

class CarinfoClass:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,carInfoModel):
       self.session.add(carInfoModel)
       if(self.session.commit()==None):
           return True
    
    def select_query(self,carInfoModel_instance):
        stmt = select(CarinfoModel.Thekey).where(
                and_(
                    CarinfoModel.CarColor == carInfoModel_instance.CarColor.strip(),
                    CarinfoModel.girbox == carInfoModel_instance.girbox.strip(),
                    CarinfoModel.OptionCond == carInfoModel_instance.OptionCond.strip(),
                    CarinfoModel.blockingAndSuspention == carInfoModel_instance.blockingAndSuspention.strip(),
                    CarinfoModel.Motor == carInfoModel_instance.Motor.strip(),
                    CarinfoModel.information == carInfoModel_instance.information.strip(),
                    CarinfoModel.Useage == carInfoModel_instance.Useage.strip(),
                    CarinfoModel.CarType ==carInfoModel_instance.CarType.strip(),
                    CarinfoModel.model==carInfoModel_instance.model.strip()
                    ))
        stmt=self.session.execute(stmt).fetchall()
        if len(stmt)  == 0:
            return None
        else:
            return stmt[0][0]

    def get(self,Thekey):
        CarInfoResults=select(CarinfoModel).where(
            and_(
                CarinfoModel.Thekey==Thekey,
            )
        )
        CarInfoResults=self.session.execute(CarInfoResults).fetchall()
        return CarInfoResults[0][0] 