from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "city" ADD "remote_id" INT NOT NULL UNIQUE;
        ALTER TABLE "city" ALTER COLUMN "name" TYPE VARCHAR(20) USING "name"::VARCHAR(20);
        ALTER TABLE "city" ALTER COLUMN "name" TYPE VARCHAR(20) USING "name"::VARCHAR(20);
        ALTER TABLE "city" ALTER COLUMN "name" TYPE VARCHAR(20) USING "name"::VARCHAR(20);
        CREATE UNIQUE INDEX "uid_city_remote__a873f0" ON "city" ("remote_id");
        CREATE UNIQUE INDEX "uid_city_name_468230" ON "city" ("name");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_city_name_468230";
        DROP INDEX "idx_city_remote__a873f0";
        ALTER TABLE "city" DROP COLUMN "remote_id";
        ALTER TABLE "city" ALTER COLUMN "name" TYPE TEXT USING "name"::TEXT;
        ALTER TABLE "city" ALTER COLUMN "name" TYPE TEXT USING "name"::TEXT;
        ALTER TABLE "city" ALTER COLUMN "name" TYPE TEXT USING "name"::TEXT;"""
